
import pymupdf
from pathlib import Path

# Step 1: Location of all PDF files
input_folder = Path(r"C:\Users\Sindhiya\Downloads\english")

# Step 2: Create an output folder
output_folder = Path("extracted_text")
output_folder.mkdir(exist_ok=True)

# Step 3: Find all PDF files
pdf_files = list(input_folder.glob("*.pdf"))

print("Total PDF files found:", len(pdf_files))

# Step 4: Keep track of successful and failed files
successful = 0
failed = 0

# Step 5: Process every PDF
for index, pdf_path in enumerate(pdf_files, start=1):

    try:
        document = pymupdf.open(pdf_path)

        full_text = ""

        # Read every page of the current PDF
        for page in document:
            full_text += page.get_text() + "\n"

        document.close()

        # Create a text file with the same name
        output_file = output_folder / (pdf_path.stem + ".txt")

        # Save the extracted text
        output_file.write_text(full_text, encoding="utf-8")

        successful += 1

        print(f"{index}/{len(pdf_files)} completed: {pdf_path.name}")

    except Exception as error:
        failed += 1
        print(f"Failed: {pdf_path.name} - {error}")

# Step 6: Display final report
print("\n----- PROCESSING SUMMARY -----")
print("Total PDFs:", len(pdf_files))
print("Successfully processed:", successful)
print("Failed:", failed)
print("Output folder:", output_folder.resolve())
