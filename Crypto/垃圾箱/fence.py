def fence(string, space):
    key = 0
    # 小于间隔继续
    while key < space:
        for i in range(0, len(string), space):
            # 不能越界
            if (i + key) < len(string):
                print(string[i + key], end="")
        key = key + 1
    print("")
str = "ssc@sc1rct0atfvbf_ei{srtse#}"
fence(str,2)