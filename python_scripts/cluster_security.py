# import os
# import json
# import pandas as pd
 
# folder_path = "../json_output/cluster_security"
# rows = []
 
# for file in os.listdir(folder_path):
#     if file.endswith(".json"):
        
#         file_path = os.path.join(folder_path, file)
        
#         with open(file_path, "r") as f:
#             data = json.load(f)
 
#         settings = data.get("settings", {})
 
#         row = {
#             "Cluster Name": file.replace(".json",""),
#             # "Cluster ID": settings.get("id"),
#             # "Name": settings.get("name"),
#             "Status": settings.get("status","-"),
#             "Agent Version": settings.get("agentVersion","-"),
#             "Last Activity": settings.get("lastActivity","-"),
#             "Features": ",".join(settings.get("features", [])),
#             "Feature Status": settings.get("featureStatus","-")
#         }
 
#         rows.append(row)
 
# df = pd.DataFrame(rows)

# # Replace empty values with "-"
# df = df.fillna("-")
# df = df.replace('', '-')
 
# df.to_excel("../xlsx_output/cluster_security.xlsx", index=False)
 
# print("Excel file created: cluster_security.xlsx")
 