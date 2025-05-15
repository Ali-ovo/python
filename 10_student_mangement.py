student_list = [
    {
        "id": "1",
        "name": "张三",
        "age": 20,
    },
    {
        "id": "2",
        "name": "李四",
        "age": 21,
    },
]


def print_info():
    print("-" * 20)
    print("welcome to student management system")
    print("1: 添加学生")
    print("2: 删除学生")
    print("3: 修改学生")
    print("4: 查询学生")
    print("5: 显示所有学生")
    print("6: 退出")
    print("-" * 20)


def choose_option(option):
    if option == "1":
        add_student()
    elif option == "2":
        delete_student()
    elif option == "3":
        modify_student()
    elif option == "4":
        query_student()
    elif option == "5":
        show_all_student()
    elif option == "6":
        exit_system()
    else:
        print("输入错误,请重新输入")


def add_student():
    stu_id = input("请输入学生id：")

    for student_info in student_list:
        if student_info["id"] == stu_id:
            print("学生已存在")
            return

    stu_name = input("请输入学生姓名：")
    stu_age = input("请输入学生年龄：")

    student_list.append({"id": stu_id, "name": stu_name, "age": stu_age})

    print("添加学生成功") 


def delete_student():
    stu_id = input("请输入学生id：")

    for student_info in student_list:
        if student_info["id"] == stu_id:
            student_list.remove(student_info)
            print("删除学生成功")
            return


def modify_student():
    stu_id = input("请输入学生id：")

    for student_info in student_list:
        if student_info["id"] == stu_id:
            student_info["name"] = input("请输入学生姓名：")
            student_info["age"] = input("请输入学生年龄：")
            print("修改学生成功")
            return

def query_student():
    stu_id = input("请输入学生id：")

    for student_info in student_list:
        if student_info["id"] == stu_id:
            print(student_info)
            return


def show_all_student():
    for student_info in student_list:
        print(student_info)


def exit_system():
    exit("系统已退出")

while True:

    print_info()

    option = input("请输入你的操作：")

    choose_option(option)

    input()
