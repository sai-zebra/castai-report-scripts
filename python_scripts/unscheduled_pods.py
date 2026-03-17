import json
import pandas as pd
import os
 
INPUT_FOLDER = "../json_output/unscheduled_pods"
OUTPUT_FILE = "../xlsx_output/unscheduled_pods.xlsx"
 
rows = []
 
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".json"):
        with open(os.path.join(INPUT_FOLDER, file)) as f:
            data = json.load(f)
 
        cluster_id = data.get("clusterId", "")
 
        for item in data.get("items", []):
            workload_name = item.get("name", "")
            namespace = item.get("namespace", "")
            workload_type = item.get("type", "")
 
            for pod in item.get("unscheduledPods", []):
                pod_name = pod.get("name", "")
                cpu = pod.get("cpuRequested", "")
                ram = pod.get("ramRequested", "")
                message = pod.get("message", "")
 
                for event in pod.get("events") or [{}]:
                    rows.append({
                        "Cluster Name": file.replace(".json", ""),
                        # "Cluster ID": cluster_id,
                        "Namespace": namespace,
                        "Workload Name": workload_name,
                        "Workload Type": workload_type,
                        "Pod Name": pod_name,
                        "CPU Requested": cpu,
                        "RAM Requested": ram,
                        "Scheduler Message": message,
                        "Event Reason": event.get("reason", ""),
                        "Event Message": event.get("message", ""),
                        # "First Timestamp": event.get("firstTimestamp", ""),
                        # "Last Timestamp": event.get("lastTimestamp", "")
                    })
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')

df.to_excel(OUTPUT_FILE, index=False)
 
print("Excel file created:", OUTPUT_FILE)
 