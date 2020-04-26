import  base64
import requests
url = "http://82a565ad15cc498796ec45c69995cc487b562fe33f004773.changame.ichunqiu.com/"
a = requests.session()
b = a.get(url)
#print(b.text)
c = b.headers['flag']
print(c)
c = base64.b64decode(c)
print(str(c))
d = str(c).split(':')
e = base64.b64decode(d[1])
print(e)
result=a.post(url,data={"ichunqiu":e})
print(result.text)