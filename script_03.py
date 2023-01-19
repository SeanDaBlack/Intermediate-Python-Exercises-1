
def letter_count(string):
    final_dict = {}
    string = string.replace(" ", "").lower()
    letter_list = list(string)

    for l in letter_list:
        final_dict.update({l: string.count(l)})

    print(final_dict)


letter_count(input("Enter a String: "))
