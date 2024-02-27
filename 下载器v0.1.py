#已知小问题：似乎此程序会现下载到根程序一个文件夹的地方 再移动到指定路径
print("下载器")
print("v0.1")
from wget import download
from time import sleep
while True :
    try:
        url = input("下载链接？")
        where = input("下载到哪个路径？")
        download(url,where)
    except Exception as e:
        print(e)
        sleep(3)
    answer = input("下载完毕，关闭程序？（y/n）")
    if answer == "y":
        break