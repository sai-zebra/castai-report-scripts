import json
import os
import pandas as pd
 
# Folder containing all cluster outputs
folder = "json_output/problematic_workloads"
 
rows = []
 
# Read all json files
for file in os.listdir(folder):
 
    if file.endswith(".json"):
 
        filepath = os.path.join(folder, file)
 
        with open(filepath) as f:
            data = json.load(f)
 
        cluster_id = data.get("clusterId")
 
        controllers = data.get("controllers", [])
 
        for controller in controllers:
 
            name = controller.get("name")
            kind = controller.get("kind")
 
            problems = controller.get("problems", [])
 
            for problem in problems:
 
                rows.append({
                    "Cluster Name": file.replace(".json",""),
                    # "Cluster ID": cluster_id,
                    "Controller Name": name,
                    "Kind": kind,
                    "Problem": problems,
                    "Standalone Pods": ";".join(controller.get("standalonePods", [])),
                    "hasProblems": ";".join(controller.get("hasProblems", []))
                })
 
 
# Convert to dataframe
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
# Save to excel
df.to_excel("xlsx_output/problematic_workloads.xlsx", index=False)
 
print("Excel file created: problematic_workloads.xlsx")
 