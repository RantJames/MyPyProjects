from itertools import product
a = ['1', '2']
b = ['3', '4']
a_n = []
b_n = []
for i in range(len(a)):
a_n.append(int(a[i]))
print(a_n)
for i in range(len(b)):
b_n.append(int(b[i]))
print(b_n)
c = (list(product(a_n, b_n)))
print(*c, sep=' ')