import json
import pandas as pd

# Load JSON data
with open("./financial_results copy 2.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Create a dictionary to store the final data for the Excel file
financial_data = {
    "Particulars": [],
    "3 months ended March 31, 2024": [],
    "Preceding 3 months ended December 31, 2023": [],
    "Corresponding 3 months ended March 31, 2023": [],
    "Year Ended March 31, 2024": [],
    "Year Ended March 31, 2023": []
}

# Populate the dictionary with data from JSON
for key, value in json_data.items():
    values = value.split()  # Split the values by space
    if len(values) == 5:  # Ensure there are exactly 5 values
        financial_data["Particulars"].append(key)
        financial_data["3 months ended March 31, 2024"].append(values[0])
        financial_data["Preceding 3 months ended December 31, 2023"].append(values[1])
        financial_data["Corresponding 3 months ended March 31, 2023"].append(values[2])
        financial_data["Year Ended March 31, 2024"].append(values[3])
        financial_data["Year Ended March 31, 2023"].append(values[4])
    elif len(values) == 3:  # Ensure there are exactly 3 values for special cases
        financial_data["Particulars"].append(key)
        financial_data["3 months ended March 31, 2024"].append(values[0])
        financial_data["Preceding 3 months ended December 31, 2023"].append(values[1])
        financial_data["Corresponding 3 months ended March 31, 2023"].append(values[2])
        financial_data["Year Ended March 31, 2024"].append("")
        financial_data["Year Ended March 31, 2023"].append("")

# Create a DataFrame from the dictionary
df = pd.DataFrame(financial_data)

# Save DataFrame to Excel
df.to_excel("financial_results.xlsx", index=False)

print("Data has been successfully saved to financial_results.xlsx.")
