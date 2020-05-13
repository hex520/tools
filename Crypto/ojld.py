def a_b_mod(a,b):# 欧几里得算法,求a,b的最小公约数
    if a>b:
        max = a
        min = b
    else:
        max = b
        min = a
    while max%min!=0:
        tmp = max%min
        if tmp>min:
            max = tmp
        else :
            max = min
            min = tmp
    return min
result = a_b_mod(10,120)
print(result)
