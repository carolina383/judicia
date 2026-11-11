
from pathlib import Path
import csv

# Folder containing all extracted judgments
folder = Path("extracted_text")

# Find all text files
text_files = list(folder.glob("*.txt"))

# Store information about each judgment
results = []

for file_path in text_files:

    text = file_path.read_text(encoding="utf-8")

    # Count characters and words
    character_count = len(text)
    word_count = len(text.split())

    results.append({
        "filename": file_path.name,
        "characters": character_count,
        "words": word_count
    })

# Find the shortest and longest judgments
shortest = min(results, key=lambda x: x["words"])
longest = max(results, key=lambda x: x["words"])

# Calculate average words
total_words = sum(item["words"] for item in results)
average_words = total_words / len(results)

# Save the analysis into a CSV file
with open("dataset_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["filename", "characters", "words"]
    )
    writer.writeheader()
    writer.writerows(results)

# Display results
print("\n--- JUDGMENT DATASET ANALYSIS ---")
print("Total judgments:", len(results))
print("Total words:", total_words)
print("Average words per judgment:", round(average_words, 2))

print("\nShortest judgment:", shortest["filename"])
print("Words:", shortest["words"])

print("\nLongest judgment:", longest["filename"])
print("Words:", longest["words"])

print("\nSummary saved as dataset_summary.csv")
