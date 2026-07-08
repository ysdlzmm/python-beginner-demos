"""
温度转换器
练习点：公式运算、分支菜单、浮点运算
"""
print("1.摄氏转华氏  2.华氏转摄氏")
choice = input("请选择转换类型：")
temp = float(input("输入温度数值："))
if choice == "1":
    f = temp * 1.8 + 32
    print(f"华氏温度：{f:.2f}")
elif choice == "2":
    c = (temp - 32) / 1.8
    print(f"摄氏温度：{c:.2f}")
else:
    print('选项错误')
