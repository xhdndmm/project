print("下载器 v0.01")
from wget import download
try:
    url = input("链接")
    where = input("路径")
    download(url,where)
except Exception as e:
    print(e)