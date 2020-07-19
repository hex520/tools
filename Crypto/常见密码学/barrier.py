#! /usr/bin/env python3
import sys
string = sys.argv[1]
space = sys.argv[2]
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
space = int(space)
fence(string,space)
