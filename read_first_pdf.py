

import pymupdf

# Location of the court judgment
pdf_path = r"C:\Users\Sindhiya\Downloads\english\2023_1_317_334_EN.pdf"

# Open the PDF
document = pymupdf.open(pdf_path)

# Store all extracted text
full_text = ""

# Read every page
for page_number, page in enumerate(document, start=1):

    text = page.get_text()

    full_text += f"\n\n--- PAGE {page_number} ---\n"
    full_text += text

# Close the PDF
document.close()

# Save extracted text into a text file
with open("judgment_text.txt", "w", encoding="utf-8") as file:
    file.write(full_text)

print("Total pages processed:", page_number)
print("Total characters extracted:", len(full_text))
print("Judgment saved successfully!")
