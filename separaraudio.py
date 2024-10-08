from pydub import AudioSegment

# Cargar el archivo de audio
audio = AudioSegment.from_wav("EncuentromujeresAfro.wav")

# Duración del audio en milisegundos (5 minutos = 300000 ms)
segment_duration = 300000

# Dividir el audio en segmentos
for i, chunk in enumerate(audio[::segment_duration]):
    chunk.export(f"segment_{i}.wav", format="wav")
