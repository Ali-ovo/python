

from dm01_student import Student
import time


class StudentCMS(object):
    def __init__(self):
        self.student_list = []

    # 显示界面
    @staticmethod
    def show_info():
        print("*" * 40)
        print('本学员管理系统V2.0完成一下操作:')
        print('\t1.添加学员')
        print('\t2.修改学员')
        print('\t3.删除学员')
        print('\t4.查询某个学员')
        print('\t5.显示所有学员')
        print('\t6.保存学员')
        print('\t0.退出系统')
        print("*" * 40)
        pass

    def add_student(self):
        name = input('请输入学员姓名:')
        age = input('请输入学员年龄:')
        gender = input('请输入学员性别:')
        mobile = input('请输入学员手机号:')
        des = input('请输入学员描述:')
        student = Student(name, age, gender, mobile, des)
        self.student_list.append(student)

    def update_student(self):
        # 2 修改学员 update_student()
        # 1 输入学员姓名update_name / 2 遍历学员信息 修改
        pass

    def del_student(self):
        del_name = input('请输入要删除的学员姓名:')
        for stu in self.student_list:
            if stu.name == del_name:
                self.student_list.remove(stu)
                print(f'{del_name} 删除成功')
                break
        else:
            print('没有找到要删除的学员')
        

    def search_student(self):
        search_name = input('请输入要查询的学员姓名:')
        for stu in self.student_list:
            if stu.name == search_name:
                print(stu)
                break
        else:
            print('没有找到要查询的学员')

    def show_all_student(self):
        for stu in self.student_list:
            print(stu)

    def save_student(self):
        with open('student.txt', 'w') as f:
            f.write(str([student.__dict__ for student in self.student_list]))
        print('保存成功')
        
        
    def load_data(self):
        with open('student.txt', 'r') as f:
            data = f.read()
            if len(data) == 0:
                self.student_list = []
            else:
                self.student_list = eval(data)
        print('加载成功')

    def start(self):
        # s1 = Student('张三', 20, "男", "111131111", "爱好AI")
        # s2 = Student('李四', 21, "男", "111131111", "爱好AI2")
        # self.student_list.append(s1)
        # self.student_list.append(s2)
        self.load_data()
        
        
        while True:
            time.sleep(1)
            print('\n')
            StudentCMS.show_info()
            num = int(input("请输入你的操作序号(数字)"))

            if num == 1:
                print('请添加学员 ')
                self.add_student()

            elif  num == 2:
                print('修改学员')
                self.update_student()

            elif  num == 3:
                print("删除学员")
                self.del_student()

            elif  num == 4:
                print('查询某个学员')
                self.search_student()

            elif  num == 5:
                print('显示所有学员信息')
                self.show_all_student()

            elif  num == 6:
                # 6  save_student()
                print('保存学员信息')
                self.save_student()

            elif  num == 0:
                str = input('你确定要退出吗(Y/y)?')
                if str.lower() == "y":
                    break
            else:
                print('请你输入数字1~6')


if __name__ == '__main__':
    studentcms = StudentCMS()
    # print(studentcms.student_list)
    studentcms.start()

