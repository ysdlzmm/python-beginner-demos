"""
简易记事本
练习点：open()、with 上下文管理器、utf-8 编码、文件读写模式
"""

# 写入内容到记事本
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("Python练习笔记\n今日学习文件操作")

# 读取文件内容
with open("note.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("记事本内容：\n", content)