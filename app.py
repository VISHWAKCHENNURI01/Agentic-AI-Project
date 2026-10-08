import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_dataframe
from src.data_profiler import detect_columns
from src.graph import build_graph


st.set_page_config(
    page_title="AI Data Analyst Agent",
    page_icon="📊",
    layout="wide"
)


st.title("📊 AI Data Analyst Agent")

st.write(
    "Upload a dataset and ask questions using "
    "Pandas + LangGraph + Gemini."
)


uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=[
        "csv",
        "xlsx",
        "xls",
        "json",
        "parquet",
        "txt"
    ]
)


if uploaded_file:

    try:

        df = load_dataframe(
            uploaded_file
        )

        st.success(
            f"Dataset loaded successfully: "
            f"{df.shape[0]} rows × {df.shape[1]} columns"
        )

    except Exception as e:

        st.error(
            f"Could not load dataset: {e}"
        )

        st.stop()


    columns = detect_columns(df)


    # ------------------------------------------------
    # Dataset Preview
    # ------------------------------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )


    # ------------------------------------------------
    # Dataset Information
    # ------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:

        st.metric(
            "Columns",
            df.shape[1]
        )

    with col3:

        st.metric(
            "Duplicates",
            int(df.duplicated().sum())
        )

    with col4:

        st.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )


    # ------------------------------------------------
    # Detected Columns
    # ------------------------------------------------

    st.subheader(
        "Detected Business Columns"
    )

    detected_data = {
        key: value
        for key, value in columns.items()
        if value is not None
    }

    if detected_data:

        st.json(
            detected_data
        )

    else:

        st.info(
            "No standard business columns were automatically detected."
        )


    # ------------------------------------------------
    # AI Data Analyst
    # ------------------------------------------------

    st.subheader(
        "Ask the AI Data Analyst"
    )

    question = st.text_input(
        "Enter your question",
        placeholder=(
            "Example: What is the total revenue?"
        )
    )


    if st.button(
        "Analyze",
        type="primary"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Analyzing dataset..."
            ):

                try:

                    graph = build_graph()

                    initial_state = {
                        "df": df,
                        "columns": columns,
                        "question": question
                    }

                    result = graph.invoke(
                        initial_state
                    )

                    answer = result.get(
                        "answer",
                        "No answer generated."
                    )

                    st.subheader(
                        "Analysis Result"
                    )

                    st.write(
                        answer
                    )

                    if result.get("route") == "local":

                        st.caption(
                            "✓ Answer calculated locally using Pandas."
                        )

                    else:

                        st.caption(
                            "✓ Answer generated using Gemini."
                        )

                except Exception as e:

                    st.error(
                        f"Analysis failed: {e}"
                    )


    # ------------------------------------------------
    # Basic Statistics
    # ------------------------------------------------

    with st.expander(
        "Statistical Summary"
    ):

        st.dataframe(
            df.describe(
                include="all"
            ).transpose(),
            use_container_width=True
        )


    # ------------------------------------------------
    # Missing Values
    # ------------------------------------------------

    with st.expander(
        "Missing Values"
    ):

        missing = (
            df.isna()
            .sum()
            .sort_values(
                ascending=False
            )
        )

        missing = missing[
            missing > 0
        ]

        if missing.empty:

            st.success(
                "No missing values found."
            )

        else:

            st.dataframe(
                missing.rename(
                    "Missing Values"
                )
            )


    # ------------------------------------------------
    # Numeric Correlation
    # ------------------------------------------------

    with st.expander(
        "Correlation Analysis"
    ):

        numeric_df = df.select_dtypes(
            include="number"
        )

        if numeric_df.shape[1] >= 2:

            correlation = (
                numeric_df.corr()
            )

            fig = px.imshow(
                correlation,
                text_auto=True,
                aspect="auto",
                title="Correlation Matrix"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info(
                "At least two numeric columns are required."
            )