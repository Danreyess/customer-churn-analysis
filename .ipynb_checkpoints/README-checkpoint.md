
---

##  Project Objectives

- Clean and preprocess the customer dataset  
- Calculate churn-related KPIs  
- Analyze factors that influence customer churn  
- Create visualizations to support findings  
- Provide business insights and strategic recommendations  

---

## Key Performance Indicators (KPIs)

These KPIs were calculated in the Jupyter Notebook:

- **Churn Rate** – Percentage of customers who left  
- **Average Monthly Charges**  
- **Average Tenure**  
- **Churn by Contract Type**  
- **Churn by Payment Method**  

---

##  Technologies Used

- Python  
- Pandas  
- Matplotlib  
- Jupyter Notebook  

---

##  Data Cleaning Steps

Data was cleaned using the `clean_churn()` function in `src/cleaning.py`:

- Converted text columns to numeric (e.g., `TotalCharges`)  
- Removed missing values  
- Converted Yes/No columns into binary  
- One-hot encoded categorical variables  
- Standardized column names  

---

## Visualizations

The following visualizations were created:

- Churn distribution bar plot  
- Churn rate by contract type (stacked bar chart)  
- Monthly charges distribution by churn  
- Tenure distribution by churn  

---

## Insights

- Customers on **month-to-month contracts** churn at a significantly higher rate.  
- Higher **monthly charges** are strongly associated with churn.  
- Customers with **low tenure** are more likely to leave early.  
- Long-term contracts (“One year” and “Two year”) show much lower churn rates.  

---

## Business Recommendations

- Encourage customers on month-to-month plans to switch to long-term contracts.  
- Offer discounts or loyalty programs for high-charge customers at risk of churn.  
- Improve onboarding and support for new customers with low tenure.  
- Provide incentives for customers paying via electronic methods with high churn rate.  

---

##  Dataset

The dataset used is a synthetic file created to simulate real customer behavior:

