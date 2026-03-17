import json
import os
import pandas as pd
 
# Folder where all cluster JSON files exist
folder = "json_output/workload_scalingpolicies"   # folder containing json files
 
rows = []
 
for file in os.listdir(folder):
    if file.endswith(".json"):
        path = os.path.join(folder, file)
 
        with open(path, "r") as f:
            data = json.load(f)
 
        for item in data.get("items", []):
 
            cluster_id = item.get("clusterId", "")
            policy_name = item.get("name", "")
            management_option = item.get("recommendationPolicies", {}).get("managementOption", "")
            apply_type = item.get("applyType", "")
            is_default = item.get("isDefault", "")
            is_readonly = item.get("isReadonly", "")
 
            cpu_function = item.get("recommendationPolicies", {}).get("cpu", {}).get("function", "")
            cpu_args = ",".join(item.get("recommendationPolicies", {}).get("cpu", {}).get("args", []))
            cpu_overhead = item.get("recommendationPolicies", {}).get("cpu", {}).get("overhead", "")
            cpu_min = item.get("recommendationPolicies", {}).get("cpu", {}).get("min", "")
 
            memory_function = item.get("recommendationPolicies", {}).get("memory", {}).get("function", "")
            memory_overhead = item.get("recommendationPolicies", {}).get("memory", {}).get("overhead", "")
            memory_min = item.get("recommendationPolicies", {}).get("memory", {}).get("min", "")
 
            confidence_threshold = item.get("recommendationPolicies", {}).get("confidence", {}).get("threshold", "")
 
            created_at = item.get("createdAt", "")
            updated_at = item.get("updatedAt", "")
 
            rows.append({
                "Cluster Name": file.replace(".json", ""),
                # "Cluster ID": cluster_id,
                "Policy Name": policy_name,
                "Management Option": management_option,
                "Apply Type": apply_type,
                "CPU Function": cpu_function,
                "CPU Args": cpu_args,
                "CPU Overhead": cpu_overhead,
                "CPU Min": cpu_min,
                # "Memory Function": memory_function,
                "Memory Overhead": memory_overhead,
                "Memory Min": round(float(memory_min), 2),
                "Confidence Threshold": confidence_threshold,
                "Is Default": is_default,
                "Is ReadOnly": is_readonly
                # "Created At": created_at,
                # "Updated At": updated_at
            })
 
# Convert to DataFrame
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
# Write to Excel
df.to_excel("xlsx_output/workload_scalingpolicies.xlsx", index=False)
 
print("Excel file created: workload_scalingpolicies.xlsx")
 