import pandas as pd
import sqlite3

df = pd.read_csv("database/healthcare_dataset.csv")

df.columns = [
    "name",
    "age",
    "gender",
    "blood_type",
    "medical_condition",
    "date_of_admission",
    "doctor",
    "hospital",
    "insurance_provider",
    "billing_amount",
    "room_number",
    "admission_type",
    "discharge_date",
    "medication",
    "test_results"
]

conn = sqlite3.connect("database/healthcare.db")

df.to_sql(
    "patients",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully.")