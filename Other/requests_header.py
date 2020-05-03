import requests,base64
def req():

    url = "http://81a4d8b0b8ab4ec3ba62a7634c64968a5724d810106642d5.changame.ichunqiu.com/"
    a = requests.session()
    b = a.get(url)
    c = b.headers['flag']
    d = base64.b64decode(c)
    d = d.decode('utf-8')
    print(d)
    e = d.split(':')
    f = base64.b64decode(e[1])
    f = f.decode('utf-8')
    body = {'ichunqiu':f}
    print(body)
    g = a.post(url,body)
    print(g.text)

    # print(e)


req()