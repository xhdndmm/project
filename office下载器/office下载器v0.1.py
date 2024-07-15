print("office下载器v0.1")
                                                             ####                                              
                                                            #####                                              
                                                             ####                                              
                                                              ###                                              
                                                              ###                                              
                                                              ###                                              
                                                              ###                                              
                   ##    #                                    ###                                              
                  ### ######         #######                  ##########    #####   ######       #######       
                 ############      ##########                 ###########   #####   ######      ############   
                ######   ####     ####    ####                ###    #####    ###      ###     ####   ######   
                 ####     ###     ###      ####               ###      ####   ###      ###     ###     ###     
                  ###     ###    ####       ###               ###      ####   ###      ###     ###     ###     
                  ###     ###    ####       ###               ###      ####   ###      ###     ###     ###     
                  ###     ###    ####       ###               ###       ###   ###      ###     ###     ###     
                  ###     ###    ####       ###               ###       ###   ###      ###      ###   ###      
                  ###     ###    ####       ###               ###      ####   ###      ###       #######       
                  ###     ###     ###      ####               ###      ###    ###      ###      ######         
                  ###     ###     ####     ###                ####   #####    ####   #####     ###             
                ###############    ####  ####                 ###########      #############   ######          
                ###############     ########                  ##  #####         ###### ####    ###########     
                                                                                       #         ###########   
                                                                                               ###       ###   
                                                                                              ###         ##   
                                                                                              ###         ##   
                                                                                              ####       ###   
                                                                                              #####    ####    
                                                                                               ###########     
                                                                                                 #######                                                                                                                      
import wget

def download(url,file):
    try:
        wget.download(url,file)
    except Exception as e:
        print("出错啦",e)

def main():
    files = input("下载到哪个路径？")
    print("以下问题请使用y或n回答")
    if input("专业增强版？") == "y":
        download("http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/zh-cn/ProPlus2021Retail.img",files)
    else:
        if input("专业版？") == "y":
            download("http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/zh-cn/Professional2021Retail.img",files)
        else:
            if input("家庭企业版？") == "y":
                download("http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/zh-cn/HomeBusiness2021Retail.img",files)
            else:
                if input("家庭学生版？") == "y":
                    download("http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/zh-cn/HomeStudent2021Retail.img",files)

while True:
    main()
    if input("下载完毕 关闭程序？") == "y":
        break