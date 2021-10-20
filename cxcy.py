import re
import time
import urllib.request
import requests

def sylu():
    fname = './sylu.txt'
    with open(fname, 'r') as f:
        lines = f.readlines() 
        last_line = lines[-1]
    f.close
    i=int(last_line)
    while(i<2000):
        uri = 'http://cxcyzx.sylu.edu.cn/info/1089/'
        url=uri+str(i)+'.htm'
        try:
            page = urllib.request.urlopen(url)
            if(page.code==200):
                html = page.read().decode('utf-8')
                title=re.findall('<title>(.+)</title>',html)
                msg=str(title)+'\t 详情链接：'+str(url)
                server(title,msg)
                print(str(title))
                i=i+1
                sylulog(i)
        except:
            i=i+1
            pass
def sylulog(i):
    fname='./sylu.txt'
    with open(fname,'a') as f :
        f.write("\n"+str(i))
def server(text, msg):
    # 将 xxxx 换成自己的server SCKEY
    uri = 'https://sc.ftqq.com/SCU168100Td7de382d19dbcd50e468feb1e988ae96606abed13f2cd.send?text={}&desp={}'.format(text, msg)
    send = requests.get(uri)

if __name__ == "__main__":
    print("正在运行....")
    while True:
        try:
            sylu()
            time.sleep(1200)
        except:
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            pass
        

