from sys import argv#使用后即可获取命令行参数

script,first,second,third = argv
#从argv中得到四个参数，只需三个，但历史惯例，脚本会有一个额外参数，scriopt是脚本名称


print(">>>>>>>>>>>argv=",repr(argv))



print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)


#powershell中输入 python ex13.py apple orange dragonfruit
#The script is called: ex13.py-----------打印出了脚本名称
#Your first variable is: apple
#Your second variable is: orange
#Your third variable is: dragonfruit

#>>>>>>>>>>>argv= ['ex13.py', 'apple', 'orange', 'dargonfruit']
#看起来像参数，目前只知道它是一个列表，python把命令行参数取来，放到列表中去，再把它们分别拆开，放到每个变量中去
