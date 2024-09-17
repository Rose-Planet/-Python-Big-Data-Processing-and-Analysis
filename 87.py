#题目：回答结果（结构体变量传递）。
#知识点：类和对象，函数

if __name__ == '__main__':
    class student:
        a = 9
        c = 0
    def o(stu):
        stu.a = 6
        stu.c = 'ccc'
    m = student()
    a = 5
    c = 3
    o(m)
    print(m.a,m.c)







