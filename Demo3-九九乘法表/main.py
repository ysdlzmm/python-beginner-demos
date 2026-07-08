"""
九九乘法表
练习点：双层 for 循环、格式化输出、制表符分隔
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    print()  # 换行
