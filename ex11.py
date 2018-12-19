print("How old are u?",end = ' ')
age = input()#引入变量age，用于获取输入，然后让python暂停等你输入，然后搜集输入内容把值赋给age
#且返回的会是字符串
print(">>>>>>>>age=",repr(age))#age为字符串，输出会有引号

print("How tall are u?",end = ' ')
height = input()

print("How much do u weigh?",end = ' ')
weight = input()

print(f"So,you're {age} old, {height} tall and {height} heavy.")

#如何获取数字
print("how old are you,baby?")
age = int(input())#当调用int函数时，即告诉python把input返回的东西转成整数再赋值给age
print(">>>>>>>>>age=",repr(age))#repr是呈现函数，会显示出变量的python模式

#用repr快速调试查看类型


#How old are u? qq
#>>>>>>>>age= 'qq'
#How tall are u? aa
#How much do u weigh? dd
#So,you're qq old, aa tall and aa heavy.
#how old are you,baby?
#12
#>>>>>>>>>age= 12
