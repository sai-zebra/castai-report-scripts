import pandas as pd
import os
 
# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xlsx_folder = os.path.join(base_dir, "xlsx_output")
output_file = os.path.join(base_dir, "cast.ai_report", "cast.ai_report.xlsx")
 
# Create Excel writer
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
 
    for file in os.listdir(xlsx_folder):
        if file.endswith(".xlsx"):
            file_path = os.path.join(xlsx_folder, file)
 
            # Read Excel
            df = pd.read_excel(file_path)
 
            # Sheet name = file name without extension
            sheet_name = os.path.splitext(file)[0]
 
            # Write to combined Excel
            df.to_excel(writer, sheet_name=sheet_name, index=False)
 
print("All Excel files merged successfully!")
print("Output file:", output_file)
 