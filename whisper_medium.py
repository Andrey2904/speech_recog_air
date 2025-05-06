from faster_whisper import WhisperModel

# Параметры
model_size = "medium"         # Модель (только английский, быстрее работает)
audio_file = "C:\\Users\\DRON\\Desktop\\speech\\ru_air_long.wav"         # Файл, который надо расшифровать
output_file = "transcription_ru.txt"

# Загружаем модель
print(f"🔄 Загружаем модель {model_size}...")
model = WhisperModel(model_size, device="cpu", compute_type="int8")  # int8 — для экономии ОЗУ



# Распознаём
print(f"🎧 Распознаём файл: {audio_file}")
segments, info = model.transcribe(audio_file, "ru")


print(f"🗣️ Язык определён: {info.language}, длительность: {info.duration:.2f} сек\n")

# Выводим по сегментам
full_text = ""
for segment in segments:
    start = segment.start
    end = segment.end
    text = segment.text.strip()
    print(f"[{start:.2f} — {end:.2f}] {text}")
    full_text += text + " "

# Сохраняем результат
with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_text.strip())

print(f"\n✅ Расшифровка завершена. Сохранено в {output_file}")
