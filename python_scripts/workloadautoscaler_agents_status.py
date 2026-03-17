import json
import pandas as pd
 
#cluster mapping
 
cluster_map = {}
 
with open("cluster_details/clusters.txt", "r") as f:
    lines = f.readlines()
 
    for line in lines:
        line = line.strip()
        if line:
            cluster_id, cluster_name = line.split(",")
            cluster_map[cluster_id.strip()] = cluster_name.strip()
 
#Load JSON file 
with open("json_output/workloadautoscaler_agents_status/workloadautoscaler_agents_status.json", "r") as f:
    data = json.load(f)
 
#Extract required fields
 
rows = []
 
for item in data["clusterAgentStatuses"]:
 
    cluster_id = item.get("clusterId")
    cluster_name = cluster_map.get(cluster_id, cluster_id)  # Fallback to ID if name not found
 
    row = {
        "Cluster Name": cluster_name,
        # "Cluster ID": cluster_id,
        "Status": item.get("status"),
        "Current Version": item.get("currentVersion"),
        "Latest Version": item.get("latestVersion"),
        "Cast Agent Version": item.get("castAgentCurrentVersion"),
        "Installed At": item.get("installedAt"),
        "Updated At": item.get("updatedAt"),
        "InPlace Resize Enabled": item.get("inPlaceResizeEnabled"),
        "Workload Autoscaler Replicas": item.get("workloadAutoscalerReplicaCount"),
        "PSI Metrics Supported": item.get("psiMetricsSupported"),
        "Resource Quotas Affecting Optimization": item.get("resourceQuotasAffectingOptimization")
    }
 
    rows.append(row)
 
#Convert to DataFrame
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
#Export to Excel
output_file = "xlsx_output/wlas_agents_status.xlsx"
 
df.to_excel(output_file, index=False)
 
print(f"Excel file created: {output_file}")
 