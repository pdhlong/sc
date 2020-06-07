import os
import sounddevice
import shutil
from scipy.io.wavfile import write

fs=44100
second=5
print("recording...")
record_voice=sounddevice.rec(int(second * fs), samplerate=fs,channels=2)
sounddevice.wait()
write("s1.wav",fs,record_voice)
newPath = shutil.move('s1.wav', 'test')
file_path = input("Enter filename:- ")
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File not found in the directory")
