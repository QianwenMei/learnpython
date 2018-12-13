#1-13创建变量，再到print，将变量作为字符串传进去
my_name = 'Zed A. Shaw'

my_age = 25

my_weight = 180

my_height = 74

my_eyes = 'Brown'

my_teeth = 'White'

my_hair = 'black'

print("Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy")
print(f"Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth  are usually {my_teeth} depending on the coffee")

#this line is tricky, try to get it exactlty  
#print("If I add %d, %d, and %d I get %d")%(my_age,my_height,my_weight,my_age+my_weight+my_height)
total = my_age + my_weight + my_height
print(F"If I add {my_age},{my_weight} and {my_height},I get {total}")