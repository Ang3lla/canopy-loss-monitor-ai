import sounddevice as sd
import scipy.io.wavfile as wav
import os

fs = 22050
seconds = 5
label = "chainsaw"

# find next available number
count = 1
while os.path.exists(f"{label}_{count}.wav"):
    count += 1

print("Recording...")

audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

filename = f"{label}_{count}.wav"
wav.write(filename, fs, audio)

print(f"Saved {filename}")