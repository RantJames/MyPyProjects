def merge_the_tools(string, k):
    # your code goes here
    split_str = []
    nk = int(len(string)/k)
    nk_ciel = math.ceil((len(string)/k))
    # print(nk_ciel)
    # print(nk)
    u_str = [['' for i in range(0)] for j in range(int(nk_ciel))]
    for index in range(0, len(string), k):
        split_str.append(string[index: index+k])
    # print(split_str)
    split_str_len = len(split_str)
    # print(split_str_len)
    for i in range(nk):
        for j in range(k):
            if split_str[i][j] not in u_str[i]:
                u_str[i].append(split_str[i][j])
    if nk < split_str_len:
        for char in (split_str[split_str_len-1]):
            if char not in u_str[split_str_len-1]:
                u_str[split_str_len-1].append(char)
    for ele in u_str:
        print(''.join(ele))