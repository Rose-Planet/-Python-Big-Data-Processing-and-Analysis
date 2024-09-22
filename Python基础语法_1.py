## 1 Python数据类型
### 1.1 字符串

#转义字符
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print ('It\'s a dog!')
print ("hello world!\nhello Python!")
print ('\\\t\\')

'''
It's a dog!
hello world!
hello Python!
\	\
'''

#原样输出引号内字符串可以使用在引号前加r
print (r'\\\t\\')

'''
\\\t\\
'''

#字符串连接与格式化输出
word1 = '"hello"'
word2 = '"world"'
sentence = word1.strip('"') + ' ' + word2.strip('"') + '!'

print( 'The first word is %s, and the second word is %s' %(word1, word2))
print (sentence)

'''
The first word is "hello", and the second word is "world"
hello world!
'''

### 1.2 整数与浮点数
print(7 ** 3)
print(7 / 3)#Python3之后，整数除法和浮点数除法已经没有差异
'''
343
2.3333333333333335
'''

#其它表示方法
print(0b1111)
print(0xff)
print(1.2e-5)
'''
15
255
1.2e-05
'''

#更多运算
import math
print (math.log(math.e)) # 更多运算可查阅文档
'''
1.0
'''

### 1.3 布尔值
print(True + False)
'''
1
'''

### 1.4 时间和日期
import time
now = time.strptime('2016-07-20', '%Y-%m-%d')
print (now)   
now = time.strftime('%Y-%m-%d', now)
print (now)   
'''
time.struct_time(tm_year=2016, tm_mon=7, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=202, tm_isdst=-1)
2016-07-20
'''

# 查看变量类型与类型转换
print(type('HEU'))
print(complex(10086))
print(type('HIT')
