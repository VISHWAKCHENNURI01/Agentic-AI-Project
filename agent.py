from src.analysis import (
    dataset_summary,
    total_revenue,
    average_revenue,
    top_products,
    category_analysis,
    region_analysis,
    statistical_summary
)


def detect_intent(question):
    q = question.lower().strip()

    if (
        "total revenue" in q
        or "total sales" in q
        or "revenue total" in q
        or "sales total" in q
    ):
        return "total_revenue"

    if (
        "average revenue" in q
        or "average sales" in q
        or "mean revenue" in q
        or "mean sales" in q
    ):
        return "average_revenue"

    if (
        "top product" in q
        or "top products" in q
        or "best product" in q
        or "highest selling product" in q
    ):
        return "top_products"

    if (
        "category" in q
        and ("revenue" in q or "sales" in q)
    ):
        return "category"

    if (
        "region" in q
        and ("revenue" in q or "sales" in q)
    ):
        return "region"

    if (
        "statistical summary" in q
        or "statistics" in q
        or "describe the data" in q
    ):
        return "statistics"

    if (
        "rows" in q
        or "columns" in q
        or "duplicates" in q
        or "missing values" in q
        or "dataset summary" in q
    ):
        return "summary"

    return "ai"


def local_analysis(df, columns, question):

    intent = detect_intent(question)

    if intent == "total_revenue":
        return total_revenue(
            df,
            columns.get("revenue")
        )

    if intent == "average_revenue":
        return average_revenue(
            df,
            columns.get("revenue")
        )

    if intent == "top_products":
        return top_products(
            df,
            columns.get("product"),
            columns.get("revenue")
        )

    if intent == "category":
        return category_analysis(
            df,
            columns.get("category"),
            columns.get("revenue")
        )

    if intent == "region":
        return region_analysis(
            df,
            columns.get("region"),
            columns.get("revenue")
        )

    if intent == "statistics":
        return statistical_summary(df)

    if intent == "summary":
        return str(dataset_summary(df))

    return None