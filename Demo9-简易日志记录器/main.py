"""
简易日志记录器
练习点：datetime 时间模块、文件追加写入 a 模式
"""
from datetime import datetime
text = input("输入要记录的日志内容：")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_text = f"[{now}] {text}\n"

# 追加写入日志，不会覆盖原有内容
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(log_text)
print("日志保存成功")
