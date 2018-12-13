# type in a whole bunch of strings, variables, and formats, and print them
types_of_people = 10
#assign 10 to types of people
x = f"there are {types_of_people}  types of people"
#assign the f-string to the x(insert type_of_people in the string)


binary = "binary"#assign "binary" to binary
do_not = "don't"#assign "don't to do_not"
y = f"those who know {binary} and those who {do_not}"#(binary,do_not)
#assign  f-string to the y(insert binary and do_not in the string)
print(x)
print(y)

print(f"I said: {x}")#x
print(f"I also said:'{y}'.")#y

hilarious = "false"
joke_evaluation = f"Isn't that joke so funny?! {hilarious}"

print (joke_evaluation) #hilarious

w = "This is the left side of ..."
e = "a string with a right side"

print (w+e)