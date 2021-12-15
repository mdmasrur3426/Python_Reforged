user_input = input("Please enter 3 numbers: ")
print(type(user_input))

string_tokens = user_input.split(",")
print(string_tokens)

int_token = []

for index in string_tokens:
    int_token.append(int(index))
a, b, c = int_token
result = int_token[0] + int_token[1] - int_token[2]

print(type(result))
