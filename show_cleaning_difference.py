
from pathlib import Path
import difflib

original = Path("extracted_text/2023_1_317_334_EN.txt")
cleaned = Path("cleaned_text/2023_1_317_334_EN.txt")

old_text = original.read_text(encoding="utf-8")
new_text = cleaned.read_text(encoding="utf-8")

difference = difflib.unified_diff(
    old_text.splitlines(),
    new_text.splitlines(),
    fromfile="Original",
    tofile="Cleaned",
    lineterm=""
)

print("\n".join(difference))
