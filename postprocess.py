import re

input_file = "transcription_ru.txt"
output_file = "transcription_ru_cleaned.txt" 
replasement_file = "replacements.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()


replasement_dict = {}

with open(replasement_file, "r", encoding="utf-8") as f:
    for line in f:
        if "=>" in line:
            wrong, correct = line.strip().split("=>", 1)
            replasement_dict[wrong.strip()] = correct.strip()

for wrong, correct in replasement_dict.items():
    pattern = r'\b' + re.escape(wrong) + r'\b'
    text = re.sub(pattern, correct, text, flags=re.IGNORECASE)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text.strip())

print(f"✅ Постобработка завершена. Сохранено в {output_file}")
