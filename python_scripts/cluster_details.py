import json
import pandas as pd
 
# #Read cluster.txt
# Format: clusterId,clusterName
 
cluster_map = {}
 
with open("cluster_details/clusters_list.txt", "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if line:
            cluster_id, cluster_name = line.split(",")
            cluster_map[cluster_id.strip()] = cluster_name.strip()
 

# to Read cluster_details.json
 
with open("json_output/cluster_details/cluster_details.json", "r") as f:
    data = json.load(f)
 
rows = []
 
# to Extract required data
 
for item in data.get("items", []):
 
    cluster_id = item.get("clusterId")
 
    row = {
        "Cluster Name": cluster_map.get(cluster_id, cluster_id),
        # "Cluster ID": cluster_id,

        "Node Count OnDemand": round(float(item.get("nodeCountOnDemand", 0)), 2),
        "Node Count Spot": round(float(item.get("nodeCountSpot", 0)), 2),
        "Node Count OnDemand Castai": round(float(item.get("nodeCountOnDemandCastai", 0)), 2),
        "Node Count Spot Castai": round(float(item.get("nodeCountSpotCastai", 0)), 2),
        "Node Count SpotFallback Castai": round(float(item.get("nodeCountSpotFallbackCastai", 0)), 2),

        "CPU Provisioned OnDemand": round(float(item.get("cpuProvisionedOnDemand", 0)), 2),
        "CPU Requested OnDemand": round(float(item.get("cpuRequestedOnDemand", 0)), 2),
        "CPU Requested Spot": round(float(item.get("cpuRequestedSpot", 0)), 2),
        "CPU Requested SpotFallback": round(float(item.get("cpuRequestedSpotFallback", 0)), 2),

        "CPU Used": round(float(item.get("cpuUsed", 0)), 2),

        "RAM Provisioned OnDemand": round(float(item.get("ramProvisionedOnDemand", 0)), 2),
        "RAM Provisioned Spot": round(float(item.get("ramProvisionedSpot", 0)), 2),
        "RAM Provisioned SpotFallback": round(float(item.get("ramProvisionedSpotFallback", 0)), 2),

        "RAM Requested OnDemand": round(float(item.get("ramRequestedOnDemand", 0)), 2),
        "RAM Requested Spot": round(float(item.get("ramRequestedSpot", 0)), 2),
        "RAM Requested SpotFallback": round(float(item.get("ramRequestedSpotFallback", 0)), 2),

        "RAM Used": round(float(item.get("ramUsed", 0)), 2),

        "Pod Count": round(float(item.get("podCount", 0)), 2),
        "Unschedulable Pods": round(float(item.get("unschedulablePodCount", 0)), 2),

        # "Node Cost OnDemand": item.get("costHourlyOnDemand"),
        # "CPU Cost Hourly OnDemand": item.get("cpuCostHourlyOnDemand"),
        # "RAM Cost Hourly OnDemand": item.get("ramCostHourlyOnDemand"),

        "Storage Provisioned": round(float(item.get("storageProvisioned", 0)), 2),
        "Storage Requested": round(float(item.get("storageRequested", 0)), 2),
        "Storage Claimed": round(float(item.get("storageClaimed", 0)), 2),
        # "Storage Cost Hourly": item.get("storageCostHourly"),

        "Cluster Score": float(item.get("clusterScore", 0))
    }
 
    rows.append(row)
 
#Convert to DataFrame
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
#Export Excel
 
df.to_excel("xlsx_output/cluster_details.xlsx", index=False)
 
print("Excel file created successfully: cluster_details.xlsx")
 