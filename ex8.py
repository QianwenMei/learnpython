formatter = "{} {} {} {}"
#告诉这个字符串，让它进行格式化
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))#true false 的打印可无需加字符串的引号，但是首字母必须大写
print(formatter.format(True,False,False,True))
#将需要格式化的字符串放到格式化字符串里四次

print(formatter.format(formatter,formatter,formatter,formatter))


print(    "I had this thing."
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")


print(formatter.format(
    "I had this thing."
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
