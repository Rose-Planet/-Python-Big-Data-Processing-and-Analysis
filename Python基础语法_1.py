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