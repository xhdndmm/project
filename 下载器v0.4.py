print("已知小问题：似乎此程序会先下载到根程序一个文件夹的地方 再移动到指定路径 且如果下载中途关闭程序 那么缓存还会保存")
print("下载器")
print("v0.4")
print("此版本增加了扫描剪贴板链接的功能")
from wget import download
from time import sleep
import urllib.request
import pyperclip
def download (url):
    try:
        url1 = url
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
                sleep(1)
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
                    print("网络连接异常：",ex)
                    print("请检查网络连接")
while True:
    try:
        things = pyperclip.paste()
    except Exception as error:
        print("似乎剪贴板里没有内容")
        answer4 = input("下载链接？")
        download(answer4)
    else:
            print("检测到剪贴板内容")
            print("具体为：",things)
            answer5 = input("是否要使用？（y/n）",)
            if answer5 == "y":
                download(things)
            else:
                answer6 = input("下载链接？")
                download(answer6)    
    answer2 = input("完成下载，关闭程序？（y/n）")
    if answer2 == "y":
        break