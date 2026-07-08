"""
简易通讯录
练习点：字典、自定义函数、while 菜单循环、数据存储
"""
contact = {}

def add_contact():
    name = input('姓名：')
    phone = input('手机号：')
    contact[name] = phone
    print('添加成功！')

def search_contact():
    name = input('请输入要查询的姓名：')
    if name in contact:
        print(f'{name}的手机号是：{contact[name]}')
    else:
        print('未找到该联系人')

def show_all():
    print('全部联系人：', contact)

while True:
    print('\n====通讯录菜单====')
    print('1.新增联系人 2.查询联系人 3.查看全部 0.退出')
    opt = input('请输入功能序号：')
    if opt == '1':
        add_contact()
    elif opt == '2':
        search_contact()
    elif opt == '3':
        show_all()
    elif opt == '0':
        print('退出通讯录')
        break
    else:
        print('输入无效，请重新选择')
