import requests
import json
import urllib
#测试

def login_web():
    url = '''http://cp6.stg3.1768.com/index.php?act=ucenter&st=login&page_index=1'''
    url2 = "http://passport2.stg3.1768.com/pass-info/oauth2/loginPassport.shtml?page_index=1&platform=ANDROID&isapp=0"
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept - Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.8",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    session = requests.session()
    session.headers = headers
    r = session.get(url, allow_redirects=False)
    r_headers = r.headers
    print(r_headers)
    data = url2Dict(r_headers["location"])
    data["loginName"] = "qlp_txz01"
    data["pwd"] = "710acf0b1f2536fca603a047b17944de511bbfa85a355b23d0b52d3dfc63e126b873327488f9ecea694c32806f40e3887c1b941bf15ae474863f202ab400979df22153f05cc2ec16060861d8db7c44fc642d6da45d5b4a4b32b6b222d4996ef71dc5abeb8270fab0feb4acc2de01caef9fd8a44e071d9b8f1c2fa069fbe86896"
    session.get(r_headers["location"], allow_redirects=False)
    r2 = session.post(url2, data=data, allow_redirects=False).headers.get("location")
    print(r2)
    session.get(r2)
    r3 = session.get("http://cp6.stg3.1768.com/?act=management")
    print(r3.text)
    # print(type(r1), r1)
    # code = json.loads(r1)
    # print(type(code), code["code"])
    # url3 = "http://caipiao6.stg3.1768.com/index.php?act=memsys&st=passportback&back=true&go_url=aHR0cCUzQSUyRiUyRmNhaXBpYW82LnN0ZzMuMTc2OC5jb20lMkZpbmRleC5waHAlM0Y=&close=0&loginChannel=paw"
    # data3 = {
    #     "act": "memsys", "st": "passportback", "back": "true",
    #     "go_url": "aHR0cCUzQSUyRiUyRmNhaXBpYW82LnN0ZzMuMTc2OC5jb20lMkZpbmRleC5waHAlM0Y=",
    #     "close": "0", "code": code["code"], "loginChannel": "paw",
    # }
    # r2 = session.post(url3, headers=headers, data=data3)
    # print(r2.url)

def reads():
    r = open("D:/Users/qilaiping/Desktop/report_2018-05-03_reslult.html")
    print(r.read())

#将url中的参数转化为字典
def url2Dict(url):
	query = urllib.parse.urlparse(url).query
	return dict([(k, v[0]) for k, v in urllib.parse.parse_qs(query).items()])



if __name__ == "__main__":
    login_web()
    # reads()

