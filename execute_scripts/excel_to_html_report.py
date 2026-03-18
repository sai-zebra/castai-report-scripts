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
<title>CAST AI Clusters Report</title>
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

.header-container{{
position:sticky;
top:0;
z-index:1000;
background:#f4f6f9;
padding-bottom:10px;
}}

.search-box{{
text-align:center;
margin:10px;
}}

input[type="text"]{{
padding:10px;
width:40%;
border-radius:5px;
border:1px solid #ccc;
}}
 
</style>
</head>
<body>
 
<div class="header-container">
<h1>CAST AI Clusters Report</h1>

<div class="search-box">
<input type="text" id="searchInput"
placeholder="Search By ClusterName..."
onkeyup="searchTable()">
    </div>
</div>
 
"""
 
# Create pages
for i, (sheet_name, df) in enumerate(sheets.items()):
    html_content += f'<div class="page" id="page{i}">'
    html_content += f'<h2 style="position:sticky;top:80px;z-index:999;">{sheet_name}</h2>'
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
 
//Search Function
function searchTable(){{
 let input = document.getElementById("searchInput").value.toLowerCase();

 for (let p=0; p<totalPages; p++){{
 let page = document.getElementById("page"+p);
 let rows = page.getElementsByTagName("tr");

 let pageHasMatch = false;

 for (let i=1; i<rows.length; i++){{
 let cells = rows[i].getElementsByTagName("td");
 let rowText="";

 for (let j=0; j<cells.length; j++){{
 rowText += cells[j].innerText.toLowerCase()+"";
 }}

 if (rowText.includes(input)){{
 rows[i].style.display="";
 pageHasMatch=true;
 }} else{{
 rows[i].style.display="none";
 }}
 }}

 //jump to page where match found
 if (pageHasMatch && input !== ""){{
 currentPage = p;
 showPage(currentPage);
 }}
 }}

 //reset if empty
 if (input === ""){{
 for (let p=0; p<totalPages; p++){{
 let page = document.getElementById("Page" + p);
 let rows = page.getElementsByTagName("tr");

 for (let i=1; i<rows.length; i++){{
 rows[i].style.display = "";
 }}
 }}
 showPage(currentPage);
 }}
}}

showPage(currentPage);
 
</script>
 
</body>
</html>
"""
 
with open(output_html, "w") as f:
    f.write(html_content)
 
print("HTML report generated", output_html)
 