import json
import os
from narwhals import col
import pandas as pd
 
folder = "json_output/efficiency_report"
rows = []
 
# Formatting functions
def cpu(v):
    return round(float(v),2) if v else ""
 
def ram(v):
    return f"{round(float(v),2)} GiB" if v else ""
 
def storage(v):
    return f"{round(float(v),2)} GiB" if v else ""
 
def percent(v):
    return f"{round(float(v),2)}%" if v else ""
 
def cost(v):
    return round(float(v),6) if v else ""
 
 
for file in os.listdir(folder):
    if file.endswith(".json"):
 
        with open(os.path.join(folder,file)) as f:
            data = json.load(f)

        items = data.get("items",{})
        summary = items.get("summary",{})
        current = items.get("current",{})
 
        row = {
 
            ("Cluster Name"): file.replace(".json",""),
            # ("Cluster","Cluster ID"): data.get("clusterId"),
 
            # Summary for the time period
            ("Summary CPU Overprov %"): percent(summary.get("cpuOverprovisioningPercent")),
            ("Summary RAM Overprov %"): percent(summary.get("ramOverprovisioningPercent")),
            ("Summary Storage Overprov %"): percent(summary.get("storageOverprovisioningPercent")),
 
            # Current used at the moment when the data was pulled, not for the time period
            ("Current CPU Overprov %"): percent(current.get("cpuOverprovisioningPercent")),
            ("Current","CPU Provisioned"): cpu(current.get("cpuProvisioned")),
            ("Current","CPU Requested"): cpu(current.get("cpuRequested")),
            ("Current","CPU Used"): cpu(current.get("cpuUsed")),
            
            ("Current RAM Overprov %"): percent(current.get("ramOverprovisioningPercent")),
            ("Current RAM Provisioned"): ram(current.get("ramGibProvisioned")),
            ("Current RAM Requested"): ram(current.get("ramGibRequested")),
            ("Current RAM Used"): ram(current.get("ramGibUsed")),

            ("Current Storage Overprov %"): percent(current.get("storageOverprovisioningPercent")),
            ("Current Storage Provisioned"): storage(current.get("storageGibProvisioned")),
            ("Current Storage Requested"): storage(current.get("storageGibRequested")),
        }
 
        rows.append(row)
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')

# df.columns = pd.MultiIndex.from_tuples(df.columns)  # this is for multi-level columns
 
df.to_excel("xlsx_output/efficiency_report.xlsx", index=False) #this index true makes to get the serial number in the excel file
 
print("Excel file created: xlsx_output/efficiency_report.xlsx successfully")
