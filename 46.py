#题目：求输入数字的平方，如果平方运算后小于 50 则退出。
#知识点：布尔值TUER/FALSE、while、if、input()、int()、def

TRUE = 1
FALSE = 0

def SQ(x):
    return x*x

a = 1
while a:
    num = int(input('请输入一个数字:'))
    print(SQ(num))
    if SQ(num) >= 50:
        a = TRUE
    else:
        a = FALSE
        

