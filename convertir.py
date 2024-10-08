from pydub import AudioSegment

audio = AudioSegment.from_file("EncuentromujeresAfro.m4a")
audio.export("EncuentromujeresAfro.wav", format="wav")
