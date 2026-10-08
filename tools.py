import pandas as pd

from langchain_core.tools import tool


# ============================================================
# DATASET SUMMARY
# ============================================================

@tool
def dataset_summary(df: pd.DataFrame) -> str:
    """
    Returns the basic structure of the dataset including
    number of rows, columns, column names, missing values
    and duplicate records.
    """

    result = []

    result.append(f"Rows: {len(df)}")
    result.append(f"Columns: {len(df.columns)}")

    result.append(
        "Columns: " +
        ", ".join(map(str, df.columns))
    )

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) > 0:

        result.append(
            "Missing values: " +
            str(missing.to_dict())
        )

    else:

        result.append(
            "Missing values: None"
        )

    result.append(
        f"Duplicate rows: {df.duplicated().sum()}"
    )

    return "\n".join(result)


# ============================================================
# TOTAL REVENUE
# ============================================================

@tool
def calculate_total_revenue(
    df: pd.DataFrame,
    revenue_column: str
) -> str:
    """
    Calculates total revenue from the specified revenue column.
    """

    if revenue_column not in df.columns:

        return (
            f"Column '{revenue_column}' "
            "does not exist."
        )

    try:

        value = pd.to_numeric(
            df[revenue_column],
            errors="coerce"
        ).sum()

        return (
            f"Total revenue: {value:,.2f}"
        )

    except Exception as e:

        return f"Revenue calculation error: {e}"


# ============================================================
# AVERAGE REVENUE
# ============================================================

@tool
def calculate_average_revenue(
    df: pd.DataFrame,
    revenue_column: str
) -> str:
    """
    Calculates average revenue from a numeric revenue column.
    """

    if revenue_column not in df.columns:

        return (
            f"Column '{revenue_column}' "
            "does not exist."
        )

    try:

        values = pd.to_numeric(
            df[revenue_column],
            errors="coerce"
        )

        value = values.mean()

        return (
            f"Average revenue: {value:,.2f}"
        )

    except Exception as e:

        return f"Average revenue error: {e}"


# ============================================================
# TOP PRODUCTS
# ============================================================

@tool
def top_products(
    df: pd.DataFrame,
    product_column: str,
    revenue_column: str,
    n: int = 5
) -> str:
    """
    Finds the top products based on total revenue.
    """

    if product_column not in df.columns:

        return f"Column '{product_column}' does not exist."

    if revenue_column not in df.columns:

        return f"Column '{revenue_column}' does not exist."

    try:

        result = (
            df.groupby(product_column)[revenue_column]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

        return result.to_string()

    except Exception as e:

        return f"Product analysis error: {e}"


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

@tool
def category_analysis(
    df: pd.DataFrame,
    category_column: str,
    revenue_column: str
) -> str:
    """
    Calculates revenue by category and identifies the
    highest-performing category.
    """

    if category_column not in df.columns:

        return (
            f"Column '{category_column}' does not exist."
        )

    if revenue_column not in df.columns:

        return (
            f"Column '{revenue_column}' does not exist."
        )

    try:

        result = (
            df.groupby(category_column)[revenue_column]
            .sum()
            .sort_values(ascending=False)
        )

        return (
            "Revenue by category:\n\n" +
            result.to_string()
        )

    except Exception as e:

        return f"Category analysis error: {e}"


# ============================================================
# REGION ANALYSIS
# ============================================================

@tool
def region_analysis(
    df: pd.DataFrame,
    region_column: str,
    revenue_column: str
) -> str:
    """
    Calculates revenue by region and identifies the
    highest-performing region.
    """

    if region_column not in df.columns:

        return (
            f"Column '{region_column}' does not exist."
        )

    if revenue_column not in df.columns:

        return (
            f"Column '{revenue_column}' does not exist."
        )

    try:

        result = (
            df.groupby(region_column)[revenue_column]
            .sum()
            .sort_values(ascending=False)
        )

        return (
            "Revenue by region:\n\n" +
            result.to_string()
        )

    except Exception as e:

        return f"Region analysis error: {e}"


# ============================================================
# QUANTITY ANALYSIS
# ============================================================

@tool
def quantity_analysis(
    df: pd.DataFrame,
    quantity_column: str
) -> str:
    """
    Calculates total and average quantity sold.
    """

    if quantity_column not in df.columns:

        return (
            f"Column '{quantity_column}' "
            "does not exist."
        )

    try:

        values = pd.to_numeric(
            df[quantity_column],
            errors="coerce"
        )

        return (
            f"Total quantity: {values.sum():,.2f}\n"
            f"Average quantity: {values.mean():,.2f}"
        )

    except Exception as e:

        return f"Quantity analysis error: {e}"


# ============================================================
# PROFIT ANALYSIS
# ============================================================

@tool
def profit_analysis(
    df: pd.DataFrame,
    profit_column: str
) -> str:
    """
    Calculates total and average profit.
    """

    if profit_column not in df.columns:

        return (
            f"Column '{profit_column}' "
            "does not exist."
        )

    try:

        values = pd.to_numeric(
            df[profit_column],
            errors="coerce"
        )

        return (
            f"Total profit: {values.sum():,.2f}\n"
            f"Average profit: {values.mean():,.2f}"
        )

    except Exception as e:

        return f"Profit analysis error: {e}"


# ============================================================
# STATISTICAL SUMMARY
# ============================================================

@tool
def statistical_summary(
    df: pd.DataFrame
) -> str:
    """
    Returns descriptive statistics for numerical columns.
    """

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.empty:

        return "No numerical columns found."

    return numeric_df.describe().round(2).to_string()