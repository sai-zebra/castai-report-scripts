import json
import os
import pandas as pd
 
folder = "../json_output/rebalancing_plan"
rows = []
 
for file in os.listdir(folder):
    if file.endswith(".json"):
        path = os.path.join(folder, file)
 
        with open(path) as f:
            data = json.load(f)
 
        for item in data.get("items", []):
            rows.append({
                "Cluster Name": file.replace(".json", ""),
                # "Cluster ID": item.get("clusterId"),
                "Rebalancing Plan ID": item.get("rebalancingPlanId"),
                # "Rebalancing Schedule ID": item.get("scheduleId"),
                "Status": item.get("status"),
                "Min Nodes": item.get("minNodes"),
                # "Created At": item.get("createdAt"),
                # "Updated At": item.get("updatedAt"),
                # "Generated At": item.get("generatedAt"),
                # "Triggered At": item.get("triggeredAt"),
                # "Created Nodes At": item.get("createdNodesAt"),
                # "Drained Nodes At": item.get("drainedNodesAt"),
                # "Deleted Nodes At": item.get("deletedNodesAt"),
                # "Finished At": item.get("finishedAt"),
                "Evict Gracefully": item.get("evictGracefully"),
                "Aggressive Mode": item.get("aggressiveMode"),
                "Execution Enabled": item.get("executionConditions", {}).get("enabled"),
                "Achieved Savings %": item.get("executionConditions", {}).get("achievedSavingsPercentage"),
                "Rebalancing Node Count": len(item.get("rebalancingNodeIds", [])),
                # "Rebalancing Node Ids": ", ".join(item.get("rebalancingNodeIds", [])),
                "Operations Count": len(item.get("operations", [])),
                "Errors Count": len(item.get("errors", []))
            })
 
df = pd.DataFrame(rows)

# Replace empty values with "-"
df = df.fillna("-")
df = df.replace('', '-')
 
df.to_excel("../xlsx_output/rebalancing_plan.xlsx", index=False)
 
print("Excel file generated: rebalancing_plan.xlsx")
 