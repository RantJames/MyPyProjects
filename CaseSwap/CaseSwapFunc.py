def case_swap(user_str):
    new_str=''
    length = len(user_str)
    for i in range(length):
        if user_str[i].isupper():
            new_str += user_str[i].lower()
        else:
            new_str += user_str[i].upper()
    return new_str

