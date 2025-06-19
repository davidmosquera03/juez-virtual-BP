import re

def remove_before_index(text):
    match = re.search(r"## Índice", text)
    return text[match.start():] if match else text


with open('data/manual.md', 'r', encoding='utf-8') as f:
     markdown_text = f.read()

# remover pie de pagina
pattern_1 = r"```\s*REPÚBLICA\s*DOMINICANA\s*```|(\#\# (Reglas Centrales|REPÚBLICA|de Debate BP))"

cleaned_text_1 = re.sub(pattern_1, "", markdown_text, flags=re.DOTALL)

pattern2 = r"(\*\*REPÚBLICA\*\*\s*\n\s*)|(\\*\*\*DOMINICANA\*\*\s)|```[^`]*fifl[^`]*```"

cleaned_text_2 = re.sub(pattern2, "", cleaned_text_1, flags=re.DOTALL)

# remover seccion antes de indice
cleaned = remove_before_index(cleaned_text_2)

output_file_path = 'data/Manual_cleaned.md' 
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned)
print(f"Cleaned content saved to {output_file_path}")