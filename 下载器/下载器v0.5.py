print("已知小问题：似乎此程序会先下载到根程序一个文件夹的地方 再移动到指定路径 且如果下载中途关闭程序 那么缓存还会保存")
print("下载器")
print("v0.5")
print("此版本优化了代码流程并精简了功能")

#⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻
#⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
#⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
#⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
#⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻
#⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼
#⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰
#⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿
#⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
#⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
#⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
#⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸

import wget
import urllib

def networktest ():
    try:
        urllib.request.urlopen("http://www.baidu.com", timeout=5)
    except Exception:
        with open('log.txt', 'w') as f:
            f.write("E:network error")
        print("网络异常")
        print("请检查网络连接是否正常")
    else:
        with open('log.txt', 'w') as f:
            f.write("E:network error")
        print("网络正常")

def download(url,file):
    wget.download(url,file)

def main():
    if input("请选择功能(输入1表示下载 输入其他东西表示测试网络)") == "1":
        url = input("链接？")
        file = input("下载路径？")
        try:
            download(url,file)
            with open('log.txt', 'w') as f:
                f.write("I:download finish")
        except Exception as e:
            with open('log.txt', 'w') as f:
                f.write("E:",e)
            print("出错啦 详细请看日志")
    else:
        networktest()

while True:
    main()