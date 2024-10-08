import speech_recognition as sr

recognizer = sr.Recognizer()
number_of_segments = 30
full_transcription = ""

for i in range(number_of_segments):
    audio_file = f"segment_{i}.wav"
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="es-ES")
            full_transcription += f"Segmento {i} transcripción: {text}\n"
        except sr.UnknownValueError:
            full_transcription += f"Lo siento, no pude entender el segmento {i}.\n"
        except sr.RequestError as e:
            full_transcription += f"Error al solicitar resultados del servicio de reconocimiento de voz para el segmento {i}; {e}\n"

# Guardar la transcripción completa en un archivo de texto
with open("transcripcion_completa.txt", "w", encoding="utf-8") as file:
    file.write(full_transcription)

print("Transcripción completa guardada en 'transcripcion_completa.txt'")
