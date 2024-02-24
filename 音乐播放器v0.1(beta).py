print("音乐播放器")
print("v0.1(beta)")
import time
import pygame
from tkinter import filedialog
import librosa
while True:
    file = filedialog.askopenfilename()
    duration = librosa.get_duration(filename=file)
    pygame.mixer.init()
    print('正在播放',file)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(duration)
    pygame.mixer.music.stop()
    print("播放完毕 请选择其他文件播放")
    time.sleep(3)