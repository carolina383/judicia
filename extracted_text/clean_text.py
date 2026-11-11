
from pathlib import Path
import re

# Folder containing extracted text
input_folder = Path("extracted_text")

# Create a folder for cleaned text
output_folder = Path("cleaned_text")
output_folder.mkdir(exist_ok=True)

# Find all text files
text_files = list(input_folder.glob("*.txt"))

successful = 0

# Clean every judgment
for file_path in text_files:

    text = file_path.read_text(encoding="utf-8")

    # Replace multiple spaces with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove unnecessary blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at the beginning and end
    text = text.strip()

    # Save cleaned text
    output_file = output_folder / file_path.name
    output_file.write_text(text, encoding="utf-8")

    successful += 1

print("Total files:", len(text_files))
print("Successfully cleaned:", successful)
print("Cleaned files saved in:", output_folder.resolve())
