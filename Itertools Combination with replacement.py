from itertools import combinations_with_replacement
from itertools import combinations

# print(list(combinations_with_replacement('1123', 3)))
# print(list(combinations('1123', 3)))

inp_str, size = input().split()
sorted_str = ''.join(sorted(inp_str))
# print(sorted_str)
iter_str = list(combinations_with_replacement(sorted_str, int(size)))
for element in iter_str:
    print(''.join(element))

