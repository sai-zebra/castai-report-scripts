import json
import pandas as pd
from datetime import datetime

def format_hr_datetime(timestamp):
    if not timestamp:
        return "-"
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", ""))
        return dt.strftime("%d-%b-%y %I:%M:%p")
    except (ValueError, OSError):
        return "-"

# Load JSON file
with open("json_output/all_clusters/all_clusters.json", "r") as f:
 data = json.load(f)
 
clusters = data.get("items", [])
 
excel_data = []
txt_lines = []
 
# Process each cluster
for cluster in clusters:
 cluster_id = cluster.get("id")
 cluster_name = cluster.get("name")
 
 # TXT output (clusterid,clustername)
 txt_lines.append(f"{cluster_id},{cluster_name}")
 
 # Extract nested fields safely
 created_at = format_hr_datetime(cluster.get("createdAt"))
 region = cluster.get("region", {}).get("name")
 status = cluster.get("status")
 provider = cluster.get("providerType")
 k8s_version = cluster.get("kubernetesVersion")
 managedBy = cluster.get("managedBy")
 reconciledAt = format_hr_datetime(cluster.get("reconciledAt"))
 
 gke = cluster.get("gke", {})
 max_pods_per_node = gke.get("maxPodsPerNode")  
 project_id = gke.get("projectId")
 
 # Tags
 tags = cluster.get("tags", {})
 product = tags.get("product")
 env = tags.get("env")
 business_unit = tags.get("business-unit")
 
 # Final row for Excel
 excel_data.append({
#  "Cluster ID": cluster_id,
 "Cluster Name": cluster_name,
 "Region": region,
 "Status": status,
 "Provider": provider,
 "K8s Version": k8s_version,
 "Product" : product,
 "Project ID": project_id,
 "Max Pods per Node": max_pods_per_node,
 "Managed By": managedBy,
 "Environment": env,
 "Business Unit": business_unit,
 "Created At": created_at,
 "Reconciled At": reconciledAt
 })
 
# Create Excel
df = pd.DataFrame(excel_data)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
df = df.replace('None', '-')
 
df.to_excel("xlsx_output/all_clusters.xlsx", index=False)
 
# Create TXT file
with open("cluster_details/clusters_list.txt", "w") as f:
 f.write("\n".join(txt_lines))

print("Excel file created: cluster_output.xlsx")
print("TXT file created: cluster_list.txt")
 