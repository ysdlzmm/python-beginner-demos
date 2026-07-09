"""
图书管理系统
整合：函数、字典、菜单循环、文件保存、增删查改
功能：录入书籍、查看库存、删除书籍、保存数据到 txt
"""
book_dict = {}

def add_book():
    name = input("书名：")
    num = input("库存数量：")
    book_dict[name] = num
    print("录入成功")

def show_book():
    print("当前库存：", book_dict)

def save_file():
    with open("book.txt", "w", encoding="utf-8") as f:
        f.write(str(book_dict))
    print("库存也保存到文件")

#主程序
while True:
    print("\n1.添加图书 2.查看库存 3.保存数据 0.退出")
    op = input("请选择功能：")
    if op == "1":
        add_book()
    elif op == "2":
        show_book()
    elif op == "3":
        save_file()
    elif op == "0":
        print("退出系统")
        break
