#开发环境：Ubuntu 22.04.4 LTS python3.10.12
import wget
url = input("下载链接？")
where = input("下载到哪个路径？")
try:
    wget.download(url,where)
except Exception as e:
    print(e)