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