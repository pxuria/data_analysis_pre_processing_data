import pandas as pd

data = pd.read_csv("./dataset/AirQualityUCI.csv",delimiter=';',skipinitialspace=True, on_bad_lines='skip')
 
 # Step 1: Drop unnecessary columns
data_cleaned = data.drop(columns=["Unnamed: 15", "Unnamed: 16"], errors='ignore')

# Step 2: Replace commas with dots in all numeric columns and convert to float
numeric_columns = ["CO(GT)", "C6H6(GT)", "T", "RH", "AH"]
for col in numeric_columns:
    data_cleaned[col] = data_cleaned[col].str.replace(',', '.').astype(float, errors='ignore')

# Step 3: Handle missing values (drop rows where essential columns are missing)
data_cleaned = data_cleaned.dropna(subset=["Date", "Time"])

# Step 4: Create a unified datetime column
data_cleaned["datetime"] = pd.to_datetime(
    data_cleaned["Date"] + " " + data_cleaned["Time"], 
    format="%d/%m/%Y %H.%M.%S", 
    errors='coerce'
)

# Step 5: Drop original Date and Time columns
data_cleaned = data_cleaned.drop(columns=["Date", "Time"], errors='ignore')

# Save the cleaned data to an Excel file
output_file_path = './output/Cleaned_AirQualityUCI.xlsx'
data_cleaned.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"Cleaned data has been saved to {output_file_path}")