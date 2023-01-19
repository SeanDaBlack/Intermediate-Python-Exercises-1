
def get_unique_list(user_list):
    return list(set(user_list))


user_input_list = [1, 2, 3, 2, 1, 4, 4]

unique_list = get_unique_list(user_input_list)
print(unique_list)
