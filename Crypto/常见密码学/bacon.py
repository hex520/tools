#培根解密,输入一个数
#input输入一个数
def bacon():
    CODE_TABLE = {  # 培根字典
        'aaaaa': 'a', 'aaaab': 'b', 'aaaba': 'c', 'aaabb': 'd', 'aabaa': 'e', 'aabab': 'f', 'aabba': 'g',
        'aabbb': 'h', 'abaaa': 'i', 'abaab': 'j', 'ababa': 'k', 'ababb': 'l', 'abbaa': 'm', 'abbab': 'n',
        'abbba': 'o', 'abbbb': 'p', 'baaaa': 'q', 'baaab': 'r', 'baaba': 's', 'baabb': 't', 'babaa': 'u',
        'babab': 'v', 'babba': 'w', 'babbb': 'x', 'bbaaa': 'y', 'bbaab': 'z'
    }
    choose = input('Input E(encode) or D(decode)\n\t')  # 输入E或D，选择加密或解密
    if choose == 'E':
        str = input('input your string:\n\t').lower()
        listStr = ''
        for i in str:
            if i in CODE_TABLE.values():
                # 将键、值各化为一个列表，取出i在value的位置后根据下标找到对应的键
                listStr += list(CODE_TABLE.keys())[list(CODE_TABLE.values()).index(i)]
        print(listStr)
        print(listStr.upper())  # 大写输出
    if choose == 'D':
        bacon = input("input your bacon:\n\t").lower()
        listBacon = []
        for i in range(0, len(bacon), 5):  # 5位为一组做一个列表
            listBacon.append(bacon[i:i + 5])
        for i in range(len(listBacon)):  # 根据下标找值
            listBacon[i] = CODE_TABLE[listBacon[i]]
        print(''.join(listBacon))
        print(''.join(listBacon).upper())
bacon()