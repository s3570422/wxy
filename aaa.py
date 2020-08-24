# name = input("plz enter your name")
# QQ = input("piz enter your QQ")
# phone = input("plz enter your phone")
# address = input("plz enter your address")

# print("Name：= %s"%name)
# print("QQ：= %d"%QQ)
# print("phone：= %d"%phone)
# print("address= %s"%address)


# name = "xiaying"
# age = 23
# addr = "melbourne"

# print("my name is %s, age is %d, address is %s"%(name,age,addr))

# me = input("出去玩吗")
# ji = input("你也出去玩吗")

# if me=="去" or ji=="去":
# 	print("我们一起出去玩....")

# AI = int(input("your ai grade"))
# CT = int(input("your ct grade"))
# SEPT = int(input("your sept grade"))

# if AI>80 and CT>80 and SEPT>80:
# 	print("your grade is hd")

import random

player = input("请输入 0剪刀 1石头 2布")

computer = random.randint(0,2)

if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
	print("赢了")
elif player == computer:
	print("输了")

else:
	print("输了")