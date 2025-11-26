import pandas as pd

def clean_churn(df):
    # 1. Strip spaces in column names
    df.columns = df.columns.str.strip()

    # 2. Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # 3. Drop rows where TotalCharges is missing
    df = df.dropna(subset=["TotalCharges"])

    # 4. Convert Yes/No columns to 1 and 0
    binary_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0})

    # 5. One-hot encode ALL remaining categorical columns
    df = pd.get_dummies(df, drop_first=True)

    return df
