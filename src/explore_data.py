import pandas as pd
customer_df=pd.read_csv(r"C:\Users\VASUNTHARA\OneDrive\Desktop\DataScience_projects\customer_churn_data_prep\data\Telco-Customer-Churn.csv")

##Phase 1 Explore Dataset

print("Dataset Shape:")
print(customer_df.shape)
print("Column Names:")
print(customer_df.columns)
print("Data Info:")
print(customer_df.info())
print("Churn Distribution:")
print(customer_df["Churn"].value_counts())
print("TotalCharges Datatype:")  # Totalcharges should be int/float but its str
print(customer_df["TotalCharges"].dtype) # confirm dtype of Totalcharges

missing_totalcharges_df = customer_df[
    customer_df["TotalCharges"] == " "] #Blank space can make column as str

print("Rows with blank TotalCharges:") #tenure*monthlycharges=Totalcharge(0*x=?)
print(missing_totalcharges_df[
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges"]])

##Phase 2 Data Quality Audit

print("Missing Values Check:")
print(customer_df.isnull().sum())  #includes only non-numeric columns

print("Unique Values Check:")
print(customer_df.nunique())

print("Duplicate Customer IDs:")
print(customer_df["customerID"].duplicated().sum())

print("Blank Value Audit:")
for col in customer_df.select_dtypes(include=str).columns:
    print(col, (customer_df[col].str.strip() == "").sum())

print("Gender Categories:")
print(customer_df["gender"].value_counts(dropna=False))

print("SeniorCitizen Categories:")
print(customer_df["SeniorCitizen"].value_counts(dropna=False))

print("Numeric Summary:")
print(customer_df.describe())  #Audit for numeric columns