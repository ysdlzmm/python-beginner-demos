"""
随机密码生成器
练习点：random、字符串拼接、循环、自定义长度
"""
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbols = "!@#$%^&*"
all_chars = letters + nums + symbols

length = int(input("设置密码长度："))
pwd = ""
for _ in range(length):
    pwd += random.choice(all_chars)
print("生成密码：", pwd)
