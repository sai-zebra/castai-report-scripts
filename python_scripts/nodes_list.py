import json
import pandas as pd
import os
 
# Folder containing all cluster JSON files
INPUT_FOLDER = "../json_output/nodes_list"
OUTPUT_FILE = "../xlsx_output/nodes_list.xlsx"
 
rows = []
 
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".json"):
 
        cluster_name = file.replace(".json", "")
        filepath = os.path.join(INPUT_FOLDER, file)
 
        with open(filepath) as f:
            data = json.load(f)
 
        for node in data.get("items", []):
 
            labels = node.get("labels", {})
            resources = node.get("resources", {})
            node_info = node.get("nodeInfo", {})
            spot = node.get("spotConfig", {})
 
            managed_by = "castai" if "provisioner.cast.ai/managed-by" in labels else node.get("cloud")
 
            rows.append({
                "Cluster Name": cluster_name,
                "Node Name": node.get("name"),
                # "Node ID": node.get("id"),
                "Cloud": node.get("cloud"),
                "Managed By": managed_by,
                "Instance Type": node.get("instanceType"),
                "Zone": node.get("zone"),
                "Spot Instance": spot.get("isSpot"),
                "State": node.get("state", {}).get("phase"),
 
                "CPU Capacity (m)": resources.get("cpuCapacityMilli"),
                "CPU Requests (m)": resources.get("cpuRequestsMilli"),
                "Memory Capacity (MiB)": resources.get("memCapacityMib"),
                "Memory Requests (MiB)": resources.get("memRequestsMib"),
 
                "OS Image": node_info.get("osImage"),
                # "Kernel Version": node_info.get("kernelVersion"),
                "Kubelet Version": node_info.get("kubeletVersion"),
 
                "Environment": labels.get("env"),
                "Business Unit": labels.get("business-unit"),
                "Node Pool": labels.get("node_pool")
            })
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
df.to_excel(OUTPUT_FILE, index=False)
 
print(f"Excel file created: {OUTPUT_FILE}")
 