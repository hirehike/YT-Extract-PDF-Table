import pdfplumber

# Path to your PDF file
pdf_file = "Fruits.pdf"

# Open the PDF file
with pdfplumber.open(pdf_file) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"Processing Page {page_number}")

        # Extract tables from the page
        tables = page.extract_tables()

        # Print the extracted tables
        for table_index, table in enumerate(tables, start=1):
            print(f"Table {table_index} on Page {page_number}")
            for row in table:
                print(row)
            print("\n" + "-" * 50 + "\n")
