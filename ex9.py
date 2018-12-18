#here's some new strange stuff, remember type it exactly.

days = "Mon Tue wen Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJuly\nAugu"
#\是转义字符，遇之，后接要么作特殊内容处理，要么作字符处理，n作特殊内容是换行
print("Here are the days:",days)

print("Here are the months:",months)
#使用三个双引号，就可以写很长的字符串，里面仍可有引号 单引号，什么都可以有哦
print("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines of we want,or 5,or 6.
""")
#python认识缩进，输出包含了空格---------任何格式化都要将文本对到最左边
