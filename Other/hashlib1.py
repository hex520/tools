import hashlib
user = "HEL1OW10rDEvery0n3"
md5encode = "12a101"
print("user:"+hashlib.md5(user.encode('utf-8')).hexdigest())
for i in range(0,9999999999):
    a = hashlib.md5(str(i).encode('utf-8')).hexdigest()
    if a[0:6] == md5encode:
        print("key"+str(i))
        exit()
#  The 7815696ecbf1c96e6894b779456d330e.php:)Welcome 8638d5263ab0d3face193725c23ce095!