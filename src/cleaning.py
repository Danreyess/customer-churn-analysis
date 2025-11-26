import pandas as pd

def clean_churn(df):
    # 1. Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # 2. Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # 3. Drop rows where TotalCharges is NaN
    df = df.dropna(subset=["TotalCharges"])

    # 4. Convert Yes/No columns to binary 1/0
    binary_cols = ["Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0})

    # 5. One-hot encode categorical variables
    df = pd.get_dummies(df, drop_first=True)

    # 6. Return cleaned DataFrame
    return df
