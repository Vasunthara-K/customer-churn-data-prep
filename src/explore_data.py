import pandas as pd
customer_df=pd.read_csv(r"C:\Users\VASUNTHARA\OneDrive\Desktop\DataScience_projects\customer_churn_data_prep\data\Telco-Customer-Churn.csv")
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