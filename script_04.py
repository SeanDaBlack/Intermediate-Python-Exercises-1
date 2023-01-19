
user_input_list = []
total = 0

while len(user_input_list) < 5:
    user_input = input(f"Enter int #{len(user_input_list)+1}: ")

    if not user_input.replace('-', '').isdigit():
        print("Invalid input. Please enter an int.")
        continue

    user_input_list.append(int(user_input))

for i in user_input_list:
    total += i

print("Your sum is", total)
