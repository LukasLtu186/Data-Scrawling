import os
from pypdf import PdfReader

file_name = "biomedicines-10-00306"

# Check if directory exists, otherwise create it
img_dir_path = file_name+"_images"
if not os.path.exists(img_dir_path):
    os.makedirs(img_dir_path)
    
txt_dir_path = file_name+"_text"
if not os.path.exists(txt_dir_path):
    os.makedirs(txt_dir_path)

reader = PdfReader(file_name+".pdf")
# reader = PdfReader(file_name+".pdf")

# Print the number of pages in the PDF
print(f"There are {len(reader.pages)} Pages")

# Get the first page (index 0) 
page = reader.pages[0]
# Use extract_text() to get the text of the page
print(page.extract_text())

# Go through every page and get the text
for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())
    file_path = os.path.join(txt_dir_path, f"Page {i+1}.txt")
    text = page.extract_text()
    print(text)
    with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(text)
    for img in page.images:
        file_path = os.path.join(img_dir_path, img.name)
        with open(file_path, "wb") as fp:
            fp.write(img.data)

# for img in page.images:
#     with open(img.name, "wb") as fp:
#             fp.write(img.data)
