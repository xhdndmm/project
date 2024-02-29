print("已知小问题：似乎此程序会先下载到根程序一个文件夹的地方 再移动到指定路径 且如果下载中途关闭程序 那么缓存还会保存")
print("已知BUG：似乎无法在linux下读取剪贴板（测试环境：Ubuntu 22.04.4 LTS python3.10.12）")
print("下载器")
print("v0.4")
print("此版本为较大更新 优化了代码流程并增加了读取剪贴板的功能")

import wget
import urllib
import pandas

def download(url,file):
    wget.download(url,file)

def networktest ():
    try:
        urllib.request.urlopen("http://www.baidu.com", timeout=5)
    except Exception:
        print("网络异常")
    else:
        print("网络正常")
    
def searchcopy ():
    try:
        searchcopyfile = str(pandas.read_clipboard)
    except Exception as er:
        print("未找到剪贴板内容...")
    else:
        return searchcopyfile

def main (url,file):
    try:
        download(url,file)
    except Exception as er:
        print("检测到异常 可能因链接或路径有错 或因网络异常 或因未识别到剪贴板内容 程序无法继续进行 报错具体为：",er)
        print("但此程序提供了几个解决办法")
        if input("是否要更换链接和路径？（y/n）") == "y":
            answer1 = input("下载链接？")
            answer2 =input("下载到哪个路径？")
            try:
                download(answer1,answer2)
            except Exception as er:
                print("又错啦 具体为：",er)
        if input("是否要进行网络检测（y/n）") == "y":
                networktest()
        print("如果还有报错那么请尝试关闭程序再打开或者重启电脑")

def start ():
    files = input("下载到哪个路径？")
    if input("是否检测剪贴板内链接？（y/n）") == "y":
        main(searchcopy(),files)
    else:
        url = input("下载链接？")
        main(url,files)

while True:
    start()
    if input("是否要关闭程序（y/n）") == "y":
        break