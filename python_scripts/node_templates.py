import os
import json
import pandas as pd
 
# Folder where all cluster JSON outputs are stored
folder_path = "../json_output/node_templates"
 
data = []
 
for file in os.listdir(folder_path):
    if file.endswith(".json"):
 
        cluster_name = file.replace(".json","")
 
        with open(os.path.join(folder_path, file)) as f:
            content = json.load(f)
 
            for item in content.get("items", []):
 
                template = item.get("template", {})
                constraints = template.get("constraints", {})
                stats = item.get("stats", {})
 
                row = {
                    "Cluster Name": cluster_name,
                    "Node Pool Name": template.get("name"),
                    "Configuration Name": template.get("configurationName"),
                    "Spot Enabled": constraints.get("spot"),
                    "OnDemand Enabled": constraints.get("onDemand"),
                    "Min CPU": constraints.get("minCpu"),
                    "Min Memory": constraints.get("minMemory"),
                    "OS": ",".join(constraints.get("os", [])),
                    "version": template.get("version"),
                    "Taint Enabled": template.get("shouldTaint"),
                    "Custom Taint Key": "; ".join([ct.get("key") for ct in template.get("customTaints", [])]),
                    "Custom Taint Value": "; ".join([ct.get("value") for ct in template.get("customTaints", [])]),
                    "Custom Taint Effect": "; ".join([ct.get("effect") for ct in template.get("customTaints", [])]),
                    "Custom Priority Families": "; ".join([",".join(cp.get("families", [])) for cp in constraints.get("customPriority", [])]),
                    "Custom Priority Spot": "; ".join([str(cp.get("spot")) for cp in constraints.get("customPriority", [])]),
                    "Custom Priority OnDemand": "; ".join([str(cp.get("onDemand")) for cp in constraints.get("customPriority", [])]),
                    "Custom Instance Enabled": template.get("customInstancesEnabled"),
                    "Custom Instances with Extended Memory": template.get("customInstancesWithExtendedMemoryEnabled"),
                    "Custom Label Key": template.get("customLabel", {}).get("key"),
                    "Custom Label Value": template.get("customLabel", {}).get("value"),
                    "Spot Nodes": stats.get("countSpot"),
                    "OnDemand Nodes": stats.get("countOnDemand"),
                    "Fallback Nodes": stats.get("countFallback")
                }
 
                data.append(row)
 
df = pd.DataFrame(data)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
df.to_excel("../xlsx_output/node_templates.xlsx", index=False)
 
print("Excel file created: all_clusters_node_templates.xlsx")
 