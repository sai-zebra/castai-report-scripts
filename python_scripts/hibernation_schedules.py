import json
import pandas as pd
 
# Load Cluster Mapping
cluster_map = {}
 
with open("cluster_details/clusters_list.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            cid, cname = line.split(",")
            cluster_map[cid.strip()] = cname.strip()
 
# Load JSON file
with open("json_output/hibernation_schedules/hibernation_schedules.json", "r") as f:
    data = json.load(f)
 
rows = []
 
for item in data["items"]:
 
    # Convert cluster IDs to cluster names
    cluster_names = []
    for c in item["clusterAssignments"]["items"]:
        cid = c["clusterId"]
        cluster_names.append(cluster_map.get(cid, cid))  # fallback if not found
 
    clusters = ", ".join(cluster_names) if cluster_names else "None"
 
    # Remove CRON_TZ from cron expressions
    pause_cron = item["pauseConfig"]["schedule"]["cronExpression"].replace("CRON_TZ=", "")
    resume_cron = item["resumeConfig"]["schedule"]["cronExpression"].replace("CRON_TZ=", "")
    # pause_cron = item["pauseConfig"]["schedule"]["cronExpression"].split()[-5]
    # pause_cron = "".join(pause_cron)
    # resume_cron = item["resumeConfig"]["schedule"]["cronExpression"].split()[-5]
    # resume_cron = "".join(resume_cron)

 
    row = {
        "Hibernation Schedule ID": item["id"],
        "Hibernation Schedule Name": item["name"],
        "Enabled": item["enabled"],
 
        "Pause Enabled": item["pauseConfig"]["enabled"],
        "Pause Cron": pause_cron,
 
        "Resume Enabled": item["resumeConfig"]["enabled"],
        "Resume Cron": resume_cron,
 
        "Instance Type": item["resumeConfig"]["jobConfig"]["nodeConfig"]["instanceType"],
 
        "Clusters": clusters
    }
 
    rows.append(row)
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('None', '-')
 
# Save to Excel
df.to_excel("xlsx_output/platform_hibernation_schedules.xlsx", index=False)
 
print("Excel file created: platform_hibernation_schedules.xlsx")
 