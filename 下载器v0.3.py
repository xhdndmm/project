#已知小问题：似乎此程序会先下载到根程序一个文件夹的地方 再移动到指定路径 且如果下载中途关闭程序 那么缓存还会保存
print("下载器")
print("v0.2")
from wget import download
from time import sleep
import urllib.request
while True :
    try:
        url1 = input("下载链接？")
        file = input("下载到哪个路径？")
        print("尝试下载",url1)
        download(url1,file)
    except Exception as e:
        print("啊！出错了",e)
        answer1 = input("是否重试？(y/n)")
        if answer1 == "y":
            try:
                download(url1,file)
            except Exception as er:
                print("还是报错，报错为：",er)
                print("尝试自动检查网络状况...")
                try:
                    urllib.request.urlopen("http://www.baidu.com", timeout=5)
                    print("网络连接正常")
                    print("请尝试更换下载链接")
                    answer3 = input("是否更换链接？（y/n）")
                    if answer3 == "y":
                        url2 = input("更改链接为？")
                        try:
                            print("尝试下载",url2)
                            download(url2,file)
                        except Exception as err:
                            print("依旧报错，报错为：",err) 
                            print("请检查链接是否有效或网络是否有问题")
                except urllib.error.URLError as ex:
                    print("网络连接异常：" + str(ex))
                    print("请检查网络连接")
    answer2 = input("完成下载，关闭程序？（y/n）")
    if answer2 == "y":
        break