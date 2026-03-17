import json
import os
import pandas as pd
 
folder = "../json_output/problematic_nodes"   # folder containing json files
rows = []
 
for file in os.listdir(folder):
    if file.endswith(".json"):
        with open(os.path.join(folder, file)) as f:
            data = json.load(f)
 
        cluster_id = data.get("clusterId")
 
        for node in data.get("nodes", []):
            node_id = node.get("nodeId")
            node_name = node.get("name")
 
            for problem in node.get("problems", []):
                rows.append({
                    "Cluster Name": file.replace(".json",""),
                    # "Cluster ID": cluster_id,
                    "Node ID": node_id,
                    "Node Name": node_name,
                    "hasProblems": problem
                })
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
df.to_excel("../xlsx_output/problematic_nodes.xlsx", index=False)
 
print("Excel file created: problematic_nodes.xlsx")
 