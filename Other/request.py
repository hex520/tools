#! /usr/bin/env python3
import requests
import json
def test():
    a = requests.session()
    b = a.get("http://192.168.0.1/cgi-bin/luci/;stok=260071bb4c012d6813c5ac568556407c/api/xqnetwork/wan_info")
    # print(b.text)
    json_text = json.loads(b.text)
    wlan_ip = json_text['info']['ipv4'][0]['ip']
    return wlan_ip
if __name__ == '__main__':
    c = test()
    print(c)
    # print(dd)
