import pandas as pd


def calculate_loss_ratio(df):
    """
    Calculate insurance loss ratio.

    Loss Ratio = Total Claims / Total Premium
    """

    total_claims = df["TotalClaims"].sum()
    total_premium = df["TotalPremium"].sum()

    if total_premium == 0:
        return 0

    loss_ratio = total_claims / total_premium

    return loss_ratio


def missing_values(df):
    """
    Return missing values count and percentage.
    """

    missing_count = df.isnull().sum()

    missing_percentage = (
        df.isnull().mean() * 100
    )

    result = pd.DataFrame({
        "Missing_Count": missing_count,
        "Missing_Percentage": missing_percentage
    })

    return result.sort_values(
        by="Missing_Percentage",
        ascending=False
    )


def province_summary(df):
    """
    Summarize insurance data by province.
    """

    summary = (
        df.groupby("Province")
        .agg(
            Total_Premium=("TotalPremium", "sum"),
            Total_Claims=("TotalClaims", "sum"),
            Policy_Count=("PolicyID", "count")
        )
        .reset_index()
    )

    summary["Loss_Ratio"] = (
        summary["Total_Claims"] /
        summary["Total_Premium"]
    )

    return summary