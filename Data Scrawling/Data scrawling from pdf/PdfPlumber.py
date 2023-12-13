import pdfplumber

with pdfplumber.open('ast_sci_data_tables_sample.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text = page.extract_text()
        print(text)
        print(page.extract_tables())