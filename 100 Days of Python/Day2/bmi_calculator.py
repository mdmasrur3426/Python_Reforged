user_height = (input("enter your height in m: "))
user_weight = (input("enter your weight in kg: "))
bmi_index = int(user_weight) / float(user_height) ** 2

print(int(bmi_index))