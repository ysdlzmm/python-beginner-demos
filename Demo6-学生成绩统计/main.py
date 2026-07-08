"""
学生成绩统计
练习点：列表遍历、求和、最值、条件筛选、平均分计算
"""
scores = [89, 72, 95, 45, 63, 77, 91]
total = sum(scores)
avg = total / len(scores)
max_score = max(scores)
min_score = min(scores)
fail = [s for s in scores if s < 60]

print(f"总分：{total}")
print(f"平均分：{avg:.1f}")
print(f"最高分：{max_score}，最低分：{min_score}")
print(f"不及格成绩：{fail}")