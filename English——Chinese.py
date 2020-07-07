from urllib import request,parse
import json

def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=headers)
    res = request.urlopen(req)
    str_json = res.read().decode('utf-8')
    myjson = json.loads(str_json)
    myjson=myjson['data']
    print(keyword,'意为：',myjson[0]['v'])
    print('更多相近词：')
    long=len(myjson)
    for i in range(1,long):
        print(myjson[i]['k'],'意为：',myjson[i]['v'])
    #info = myjson['data'][0]['v']
    #print(info)

if __name__ == '__main__':
    while True:
        keyword = input('需要翻译的单词：')
        if keyword == '':
            break
        try:
            fanyi(keyword)
        except IndexError:
            print('未知错误！也许是该词未收录')
input('谢谢使用，回车退出')
