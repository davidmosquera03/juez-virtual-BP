import re


with open('data/manual.md', 'r', encoding='utf-8') as f:
     markdown_text = f.read()

# Define the pattern to remove, handling potential variations in whitespace/newlines
# re.DOTALL makes '.' match newlines, allowing for the multi-line pattern.
pattern_to_remove = r"```\s*REPÚBLICA\s*DOMINICANA\s*```"

# Remove all occurrences of the pattern
cleaned_markdown_text = re.sub(pattern_to_remove, "", markdown_text, flags=re.DOTALL)

pattern2 = r"(\*\*REPÚBLICA\*\*\s*\n\s*)|(\\*\*\*DOMINICANA\*\*\s)"

cleaned_markdown_text2 = re.sub(pattern2, "", cleaned_markdown_text, flags=re.DOTALL)

output_file_path = 'data/Manual_cleaned.md' # Or overwrite the original: 'your_file.md'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned_markdown_text2)
print(f"Cleaned content saved to {output_file_path}")