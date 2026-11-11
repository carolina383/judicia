
from pathlib import Path

original_folder = Path("extracted_text")
cleaned_folder = Path("cleaned_text")

changed = 0
unchanged = 0

for original_file in original_folder.glob("*.txt"):

    cleaned_file = cleaned_folder / original_file.name

    original_text = original_file.read_text(encoding="utf-8")
    cleaned_text = cleaned_file.read_text(encoding="utf-8")

    if original_text == cleaned_text:
        unchanged += 1
    else:
        changed += 1

print("\n--- CLEANING COMPARISON REPORT ---")
print("Total files:", changed + unchanged)
print("Files where formatting changed:", changed)
print("Files with no visible text changes:", unchanged)
