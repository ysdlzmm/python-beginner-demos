"""
猜数字小游戏（经典循环练习）
练习点：random随机数、while 循环、计数、多分支判断
"""
import random
target = random.randint(1, 100)  # 生成一个1到100之间的随机整数
count = 0
print("猜数字游戏！范围：1～100")

while True:
    guess = int(input("请输入你猜的数字："))
    count += 1
    if target < guess:
        print("猜大了，再试试！")
    elif target > guess:
        print("猜小了，再试试！")
    else:
        print(f"恭喜猜对了！总共猜了{count}次")
        break
