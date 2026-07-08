"""
简易四则计算器
练习点：input()、类型转换、if 分支、除数为 0 异常判断
"""
print("===简易四则计算器===")
num1 = float(input("输入第一个数字："))
op = input("输入运算符(+ - * /)：")
num2 = float(input("输入第二个数字："))

res = ""
if op == '+':
    res = num1 + num2
elif op == '-':
    res = num1 - num2
elif op == '*':
    res = num1 * num2
elif op == '/':
    if num2 == 0:
        res = "错误：除数不能为零！"
    else:
        res = num1 / num2
else:
    res = "运算符无效"
print(f"计算结果：{str(res)}")
