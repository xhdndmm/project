#目前已知BUG：似乎无法在linux下运行（测试环境：Ubuntu 22.04.4 LTS)
print("music player")
print("v0.1")
import time
from pygame import mixer
from tkinter import filedialog
from librosa import get_duration
while True:
    file = filedialog.askopenfilename()
    duration = get_duration(path=file)
    mixer.init()
    print('正在播放：',file)
    mixer.music.load(file)
    mixer.music.play()
    time.sleep(duration)
    mixer.music.stop()
    print("播放完毕 请选择其他文件播放")
    time.sleep(1)