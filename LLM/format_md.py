import re

def remove_before_index(text):
    match = re.search(r"## Índice", text)
    return text[match.start():] if match else text


with open('data/manual.md', 'r', encoding='utf-8') as f:
     markdown_text = f.read()
# remover pie de pagina
pattern_to_remove = r"```\s*REPÚBLICA\s*DOMINICANA\s*```|(\#\# (Reglas Centrales|REPÚBLICA|de Debate BP))"

cleaned_markdown_text = re.sub(pattern_to_remove, "", markdown_text, flags=re.DOTALL)

pattern2 = r"(\*\*REPÚBLICA\*\*\s*\n\s*)|(\\*\*\*DOMINICANA\*\*\s)"

cleaned_markdown_text2 = re.sub(pattern2, "", cleaned_markdown_text, flags=re.DOTALL)

# remover seccion antes de indice
cleaned = remove_before_index(cleaned_markdown_text2)

output_file_path = 'data/Manual_cleaned.md' # Or overwrite the original: 'your_file.md'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned)
print(f"Cleaned content saved to {output_file_path}")