like = ["icecream", "chocolate", "pizza"]
dislike = ["matha", "chotomach", "narikel"]
soso = ["mach", "nuts", "allergy"]
map_all = [like, dislike, soso]
print(map_all)
position = input("Where do you want to put the treasure? ")
position_one = int(position[0]) - 1
position_two = int(position[1]) - 1
print(position_one)
print(position_two)

x_position = map_all[position_two][position_one]

print(x_position)