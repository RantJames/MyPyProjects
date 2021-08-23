import collections
from collections import Counter


# mylist = [1, 1, 1, 2, 4, 4, 4, 5]
# print(Counter(mylist))
# print(Counter(mylist).items())
# print(Counter(mylist).keys())
# print(Counter(mylist).values())

numshoes = input('>')
shoes = collections.Counter(map(int, input('>').split()))
numCust = int(input('>'))

income = 0

for i in range(numCust):
    size, price = map(int, input('>').split())
    if shoes[size]:
        income = income + price
        shoes[size] -= 1

print(income)