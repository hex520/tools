# import matplotlib.pyplot as plt
# import random
#
# x1 = list(range(10))
# y1 = [random.randint(0, 10) for i in range(10)]
# plt.plot(x1, y1, color='r', markerfacecolor='blue', marker='o')
# for a, b in zip(x1, y1):
# 	plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)
#
# plt.legend()
# plt.show()
import  matplotlib as mpl
import  matplotlib.pyplot as plt
import  re
# plt.plot(x,y)
# plt.plot(1,2,"*")
# plt.show()
with open('./meihuai.jpg','r') as h:
    h=h.read()
tem=''
tem_str = ''
for i in range(0,len(h)-1,2):
	tem='0x'+h[i]+h[i+1]
	tem=int(tem,base=16)
	a =  chr(tem)
	# print(a)
	if a =='\n':
		# print(tem_str,end='')
		b =  tem_str.replace('(','')
		b = b.replace(')','')
		b = b.split(',')
		# b = tem_str.split(',')
		# print(b[0])
		plt.plot(int(b[0]),int(b[1]),"*")
		tem_str = ''
	if a !='\n':
		tem_str += a

plt.show()

		# tem_str+=chr(ten)
	# print(tem_str)





# file = open('./meihuai.jpg','r',encoding='utf-8')
# a = file.read()
# print(a)
# b = len(a)
# print(b/2)
# tem_num = file.read()
# tem_len = len(tem_num)
# print(tem_num)
# print('len:%d' % tem_len)
# i = 0
# while i < tem_len/2:
# 	tem_hex = tem_num[i:i+2]
# 	print(tem_hex)
	# tem_int = int(tem_hex, 16)
	# tem_asc = chr(tem_int)
	# print(tem_asc,end='')
	# i+=2
# while 1:

	# if file.read()=='EOF':
	# 	break



