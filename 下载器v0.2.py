#已知小问题：似乎此程序会先下载到根程序一个文件夹的地方 再移动到指定路径 且如果下载中途关闭程序 那么缓存还会保存
print("下载器")
print("v0.2")
print("此版本增加了下载失败重试这个功能")
from wget import download
from time import sleep
while True :
    try:
        url = input("下载链接？")
        file = input("下载到哪个路径？")
        print("尝试下载")
        download(url,file)
    except Exception as e:
        print("啊！出错了",e)
        answer1 = input("是否重试？(y/n)")
        if answer1 == "y":
            try:
                download(url,file)
            except Exception as er:
                print("还是报错，将自动结束程序...")
                print("报错为：",e)
                sleep(1)
                break
    answer2 = input("完成下载，关闭程序？（y/n）")
    if answer2 == "y":
        break