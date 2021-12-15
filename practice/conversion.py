string_array = ["1.1", "2.2", "3.3"]
print(string_array)

int_array = []
for num in string_array:
    int_num = float(num)
    int_array.append(int_num)

return int_array