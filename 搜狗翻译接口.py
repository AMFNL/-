'''
搜狗翻译接口。
'''



import requests

def translation (word):
    url = "https://fanyi.sogou.com/reventondc/suggV3"
    date ={
        'uuid': '325e6d13-7aa5-4a2e-8ae7-aedb2739aff4',
        'addSugg': 'on',
        'pid': 'sogou-dict-vr',
        'from': 'auto',
        'to': 'zh-CHS',
        'client': 'web',
        'text': word
    }
    head ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'

    }

    resp = requests.post(url=url,headers=head,data=date)
    result = resp.json()
    print(result["sugg"][0]["k"],'==>',result["sugg"][0]["v"])
while True:
    word = input("请输入要翻译的词句：")
    if word=="117":
        break
    try:
        translation(word)
    except:
        print("翻译失败!")