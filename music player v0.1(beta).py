print("music player")
print("v0.1(beta)")
import time
from pygame import mixer
from tkinter import filedialog
from librosa import get_duration
while True:
    file = filedialog.askopenfilename()
    duration = get_duration(path=file)
    mixer.init()
    print('now playing',file)
    mixer.music.load(file)
    mixer.music.play()
    time.sleep(duration)
    mixer.music.stop()
    print("after playing please select another file to play")
    time.sleep(1)