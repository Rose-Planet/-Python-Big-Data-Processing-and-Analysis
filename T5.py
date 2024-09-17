#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#知识点：列表list,输入input(),int(),append(),sort(),print(),for

l = []
for i in range(3):
    x = int(input('整数：\n'))
    l.append(x)
l.sort()
print(l)


