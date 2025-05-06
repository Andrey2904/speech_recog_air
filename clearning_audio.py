import noisereduce as nr
import numpy as np
import soundfile as sf

INPUT_FILE = "C:\\Users\\DRON\\Desktop\\speech\\ATIS_Aeroporta_Pulkovo_USB_SDR_Priemnik_udalenie_ot_porta_24_km.wav"
OUTPUT_FILE = "denoised.wav"

# Загружаем WAV-файл
data, rate = sf.read(INPUT_FILE)
print(f"Файл загружен: {INPUT_FILE}, частота: {rate} Гц, длина: {len(data)/rate:.2f} сек")

# Если стерео — берём только один канал
if len(data.shape) == 2:
    print("Стерео обнаружено — берём только один канал")
    data = data[:, 0]

# Пример: используем первые 0.5 сек как шумовой профиль
noise_sample = data[0:int(rate * 0.5)]

# Убираем шум
reduced_noise = nr.reduce_noise(y=data, sr=rate, y_noise=noise_sample)

# Сохраняем результат
sf.write(OUTPUT_FILE, reduced_noise, rate)
print(f"Очищенное аудио сохранено в: {OUTPUT_FILE}")
