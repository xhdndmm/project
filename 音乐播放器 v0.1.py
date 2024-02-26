#目前已知BUG
#似乎无法在linux下运行（测试环境：Ubuntu 22.04.4 LTS python3.10.12)
#似乎播放完音乐不能再次选择音乐（虽然程序在运行但似乎没有任何反应 作者尝试注释掉第17行代码 可以正常选择 但这行代码必须有 不然无法播放）（此BUG测试环境为win10 22H2 python3.10.8)
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