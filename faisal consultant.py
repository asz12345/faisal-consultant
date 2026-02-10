import zipfile
import os
import shutil

# مسار ملفات PDF التي سبق تجهيزها
pdf_path = "/mnt/data/Faisal_Consultant_Profile.pdf"

# مسار ZIP النهائي
zip_file_path = "/mnt/data/Faisal_Consultant_Website_Final.zip"

# إنشاء مجلد مؤقت
temp_dir = "/mnt/data/faisal_website_final"
os.makedirs(temp_dir, exist_ok=True)

# إنشاء ملفات الموقع الرئيسية
index_html = """<html>
<head>
  <link rel='stylesheet' href='style.css'>
</head>
<body>
  <h1>Faisal Consultant</h1>
  <p>Civil Engineer & Executive Management Advisor</p>
  <a href='assets/Faisal_Consultant_Profile.pdf' download>Download PDF</a>
  <script src='script.js'></script>
</body>
</html>"""

style_css = """body { font-family: Arial, sans-serif; text-align: center; background-color: #f5f5f5; color: #333; }
h1 { color: #1a202c; margin-top: 50px; }
a { text-decoration: none; background-color: #4f46e5; color: #fff; padding: 10px 20px; border-radius: 20px; }"""

script_js = "console.log('Faisal Consultant Website Loaded');"

# حفظ الملفات في الجذر
with open(os.path.join(temp_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
with open(os.path.join(temp_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)
with open(os.path.join(temp_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(script_js)

# إنشاء مجلد assets ونسخ PDF
assets_dir = os.path.join(temp_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
shutil.copy(pdf_path, os.path.join(assets_dir, "Faisal_Consultant_Profile.pdf"))

# إنشاء ZIP النهائي
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, temp_dir)
            zipf.write(file_path, arcname=arcname)

# تنظيف المجلد المؤقت
shutil.rmtree(temp_dir)

zip_file_path
