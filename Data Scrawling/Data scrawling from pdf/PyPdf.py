import os
from pypdf import PdfReader
from os import listdir
from os.path import isfile, join

# Get base path
mypath = os.getcwd()
# print(os.path.basename(mypath))

# Check if directory is correct. If default directory is with python files or below this directory with other folder with pdf files
if os.path.basename(mypath) == "Data scrawling from pdf":
   mypath = os.path.split(mypath)[0]
   os.chdir(mypath)
#    print(mypath)

# Get list of all pdf files from "PDF_files" folder 
mypath = os.path.join(mypath, "PDF_files")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Check if directory exists, otherwise create it
def check_dir_existence(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Goes through all pdf files and get scrawled data like text from every pages and images
for i in  range (0, len(onlyfiles)):
    file_name = onlyfiles[i].replace(".pdf", "")
    
    # Directories paths
    data_dir_path = "Pdf_file_data"
    img_dir_path = os.path.join(data_dir_path, file_name+"_images")
    txt_dir_path = os.path.join(data_dir_path, file_name+"_text")
    
    # Read pdf file
    reader = PdfReader(os.path.join(mypath, file_name+".pdf"))

    # Print the number of pages in the PDF and file name
    print(f"There are {len(reader.pages)} Pages in {file_name}")
    print()

    # Go through every page and get the text
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        check_dir_existence(txt_dir_path)
        file_path = os.path.join(txt_dir_path, f"Page {i+1}.txt")
        text = page.extract_text()
        print(text)
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(text)
        # Go through page and get images
        for img in page.images:
            check_dir_existence(img_dir_path)
            file_path = os.path.join(img_dir_path, img.name)
            with open(file_path, "wb") as fp:
                fp.write(img.data)
