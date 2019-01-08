from sys import argv#使用后即可获取命令行参数

script,first,second,third = argv
#从argv中得到四个参数，只需三个，但历史惯例，脚本会有一个额外参数，scriopt是脚本名称

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
