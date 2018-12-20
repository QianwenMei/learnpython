#new
age = input("How old are you?")
print(">>>>>>>>>age=",repr(age))

height = input("How tall are you?")

weight = input("How much do you weigh?")

print(f"So,you're {age} old,{height} tall and {weight} heavy.")

#before
print("How old are you?",end = ' ')
age = input()
print(f"So you are {age} old.")
print(">>>>>>>>>age=",repr(age))