import json
import pandas as pd
 
# Load JSON file
with open("json_output/platform_usage_report/platform_usage_report.json", "r") as f:
    data = json.load(f)
 
rows = []
 
# Loop through features
for feature in data.get("features", []):
 
    row = {
        "Feature": feature.get("feature"),
        "Display Name": feature.get("displayName"),
        "Usage": feature.get("usage"),
        "Unit": feature.get("unit"),
        "Credits Applied": feature.get("creditsApplied"),
        "Is Free Of Charge": feature.get("freeOfCharge", {}).get("isFreeOfCharge")
    }
 
    rows.append(row)
 
# Convert to dataframe
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
# Save to Excel
df.to_excel("xlsx_output/platform_usage_report.xlsx", index=False)
 
print("Excel file created: platform_usage_report.xlsx")
 