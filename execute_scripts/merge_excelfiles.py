import pandas as pd
import os

# List the exact names of the Excel files in the order you want them to appear
ordered_files = [
    "all_clusters.xlsx",
    "cluster_details.xlsx",
    "efficiency_report.xlsx"
]

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xlsx_folder = os.path.join(base_dir, "xlsx_output")
output_file = os.path.join(base_dir, "cast.ai_report", "cast.ai_report.xlsx")

# Create Excel writer
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    
    # Process the files in the specified order
    for file_name in ordered_files:
        file_path = os.path.join(xlsx_folder, file_name)
        
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            sheet_name = os.path.splitext(file_name)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Successfully added {file_name} as a sheet.")
        else:
            print(f"Warning: The file '{file_name}' was not found and has been skipped.")

    # Get a list of all files already processed
    processed_files = set(ordered_files)
    
    # Get all .xlsx files from the directory
    all_xlsx_files = [f for f in os.listdir(xlsx_folder) if f.endswith(".xlsx")]
    
    # Determine which files are remaining
    remaining_files = [f for f in all_xlsx_files if f not in processed_files]

    if remaining_files:
        print("\nAdding remaining files...")
        for file_name in remaining_files:
            file_path = os.path.join(xlsx_folder, file_name)
            df = pd.read_excel(file_path)
            sheet_name = os.path.splitext(file_name)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Successfully added remaining file: {file_name}")

print("All Excel files merged successfully!")
print("Output file:", output_file)
