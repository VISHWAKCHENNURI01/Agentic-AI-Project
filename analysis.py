import pandas as pd


def dataset_summary(df):

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df.isna().sum().sum())
    }


def total_revenue(df, revenue_column):

    if not revenue_column:
        return "Revenue column was not found."

    value = pd.to_numeric(
        df[revenue_column],
        errors="coerce"
    ).sum()

    return f"Total revenue: {value:,.2f}"


def average_revenue(df, revenue_column):

    if not revenue_column:
        return "Revenue column was not found."

    value = pd.to_numeric(
        df[revenue_column],
        errors="coerce"
    ).mean()

    return f"Average revenue: {value:,.2f}"


def top_products(
    df,
    product_column,
    revenue_column,
    n=5
):

    if not product_column:
        return "Product column was not found."

    if not revenue_column:
        return "Revenue column was not found."

    temp = df.copy()

    temp[revenue_column] = pd.to_numeric(
        temp[revenue_column],
        errors="coerce"
    )

    result = (
        temp.groupby(product_column)[revenue_column]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    return result.to_string()


def category_analysis(
    df,
    category_column,
    revenue_column
):

    if not category_column:
        return "Category column was not found."

    if not revenue_column:
        return "Revenue column was not found."

    temp = df.copy()

    temp[revenue_column] = pd.to_numeric(
        temp[revenue_column],
        errors="coerce"
    )

    result = (
        temp.groupby(category_column)[revenue_column]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def region_analysis(
    df,
    region_column,
    revenue_column
):

    if not region_column:
        return "Region column was not found."

    if not revenue_column:
        return "Revenue column was not found."

    temp = df.copy()

    temp[revenue_column] = pd.to_numeric(
        temp[revenue_column],
        errors="coerce"
    )

    result = (
        temp.groupby(region_column)[revenue_column]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_string()


def statistical_summary(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return "No numeric columns available."

    return numeric_df.describe().round(2).to_string()