import pandas as pd


def load_dataframe(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, engine="openpyxl")

    elif file_name.endswith(".xls"):
        df = pd.read_excel(uploaded_file, engine="xlrd")

    elif file_name.endswith(".json"):
        df = pd.read_json(uploaded_file)

    elif file_name.endswith(".parquet"):
        df = pd.read_parquet(uploaded_file)

    elif file_name.endswith(".txt"):
        try:
            df = pd.read_csv(uploaded_file, sep=",")
        except Exception:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, sep="\t")

    else:
        raise ValueError(
            "Unsupported file type. "
            "Use CSV, XLSX, XLS, JSON, Parquet or TXT."
        )

    return df