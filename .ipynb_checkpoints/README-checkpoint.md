Customer Churn Analysis

A Data Analytics project by Dani Reyes

This project analyzes customer churn using a synthetic dataset modeled after the Telco Customer Churn dataset. The goal is to understand why customers leave, calculate key business KPIs, visualize patterns, and provide actionable insights to reduce churn.

Objective

Identify the key factors that drive customer churn and provide business recommendations to improve customer retention.

Technologies Used

Python

Pandas

Matplotlib

Jupyter Notebook

Data Cleaning

Data was cleaned using a custom function (clean_churn) that:

Removed unnecessary spaces

Converted string values to numeric when needed

Fixed missing values

Encoded categorical variables

Converted Yes/No values into 1/0

Applied one-hot encoding to all remaining categoricals

Key Performance Indicators (KPIs)

Churn Rate

Average Monthly Charges

Average Tenure

Churn by Contract Type

Churn by Payment Method

Visual Analysis

Churn Distribution

Churn Rate by Contract Type

Monthly Charges vs Churn

Tenure vs Churn

Insights

Customers with Month-to-Month contracts churn the most.

Higher Monthly Charges correlate strongly with churn.

New customers (low tenure) leave at higher rates.

Senior Citizens show higher churn.

Electronic Check users churn disproportionately more.

Customers with more add-on services tend to stay longer.

Business Recommendations

Offer retention incentives for Month-to-Month customers.

Reevaluate pricing or offer discounts to high-charge customers.

Improve the onboarding process for new customers.

Create support programs for Senior Citizens.

Provide incentives to switch from Electronic Check to more stable payment methods.

Promote bundles to increase customer stickiness.

Conclusion

This analysis provides a clear understanding of churn patterns and presents strategic recommendations that can directly help reduce customer turnover and improve business performance.