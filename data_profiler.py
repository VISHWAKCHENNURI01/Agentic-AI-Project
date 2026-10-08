def find_column(df, keywords):

    for column in df.columns:

        column_lower = str(column).lower()

        for keyword in keywords:

            if keyword in column_lower:
                return column

    return None


def detect_columns(df):

    return {
        "revenue": find_column(
            df,
            [
                "revenue",
                "sales",
                "amount",
                "income",
                "turnover"
            ]
        ),

        "quantity": find_column(
            df,
            [
                "quantity",
                "qty",
                "units"
            ]
        ),

        "profit": find_column(
            df,
            [
                "profit",
                "margin",
                "earnings"
            ]
        ),

        "category": find_column(
            df,
            [
                "category",
                "segment",
                "type"
            ]
        ),

        "region": find_column(
            df,
            [
                "region",
                "state",
                "city",
                "country",
                "location"
            ]
        ),

        "product": find_column(
            df,
            [
                "product",
                "item",
                "sku"
            ]
        ),

        "customer": find_column(
            df,
            [
                "customer",
                "client",
                "buyer"
            ]
        ),

        "date": find_column(
            df,
            [
                "date",
                "time",
                "month",
                "year"
            ]
        )
    }