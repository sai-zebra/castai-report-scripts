import pandas as pd
import os
 
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
excel_file = os.path.join(base_dir, "cast.ai_report", "cast.ai_report.xlsx")
output_html = os.path.join(base_dir, "cast.ai_report", "castai_report.html")
 
# Read all sheets
sheets = pd.read_excel(excel_file, sheet_name=None)
 
sheet_names = list(sheets.keys())
 
html_content = f"""
<html>
<head>
<title>CAST AI Cluster Report</title>
<style>
 
body{{
font-family: Arial;
background:#f4f6f9;
padding:20px;
}}
 
h1{{
text-align:center;
color:#333;
}}
 
h2{{
background:#2c3e50;
color:white;
padding:10px;
border-radius:5px;
}}
 
table{{
border-collapse: collapse;
width:100%;
margin-bottom:40px;
background:white;
}}
 
th, td{{
border:1px solid #ddd;
padding:8px;
text-align:left;
}}
 
th{{
background:#3498db;
color:white;
}}
 
tr:nth-child(even){{
background:#f2f2f2;
}}
 
.page {{
display: none;
}}
 
.active {{
display: block;
}}
 
.nav-buttons {{
text-align:center;
margin-top:20px;
position: sticky;
bottom: 0;
background: #f4f6f9;
padding: 10px;
}}
 
button {{
padding:10px 20px;
margin:5px;
border:none;
background:#3498db;
color:white;
border-radius:5px;
cursor:pointer;
}}
 
button:disabled {{
background:grey;
cursor:not-allowed;
}}
 
select {{
padding:8px;
margin:5px;
border-radius:5px;
}}
 
</style>
</head>
<body>
 
<h1>CAST AI Cluster Report</h1>
 
"""
 
# Create pages
for i, (sheet_name, df) in enumerate(sheets.items()):
    html_content += f'<div class="page" id="page{i}">'
    html_content += f"<h2>{sheet_name}</h2>"
    html_content += df.to_html(index=False)
    html_content += "</div>"
 
# Navigation at bottom (NEW POSITION + DROPDOWN)
html_content += f"""
<div class="nav-buttons">
 
<button onclick="prevPage()">Previous</button>
 
<select id="pageSelect" onchange="goToPage()">
"""
 
# Dropdown options
for i, name in enumerate(sheet_names):
    html_content += f'<option value="{i}">{name}</option>'
 
html_content += """
</select>
 
<span id="pageInfo"></span>
 
<button onclick="nextPage()">Next</button>
 
</div>
"""
 
# JavaScript
html_content += f"""
<script>
 
let currentPage = 0;
let totalPages = {len(sheet_names)};
 
function showPage(index) {{
    for (let i = 0; i < totalPages; i++) {{
        document.getElementById("page" + i).classList.remove("active");
    }}
    document.getElementById("page" + index).classList.add("active");
 
    document.getElementById("pageInfo").innerText = 
        "Page " + (index + 1) + " of " + totalPages;
 
    document.getElementById("pageSelect").value = index;
}}
 
function nextPage() {{
    if (currentPage < totalPages - 1) {{
        currentPage++;
        showPage(currentPage);
    }}
}}
 
function prevPage() {{
    if (currentPage > 0) {{
        currentPage--;
        showPage(currentPage);
    }}
}}
 
function goToPage() {{
    let selected = document.getElementById("pageSelect").value;
    currentPage = parseInt(selected);
    showPage(currentPage);
}}
 
showPage(currentPage);
 
</script>
 
</body>
</html>
"""
 
with open(output_html, "w") as f:
    f.write(html_content)
 
print("HTML report generated", output_html)
 