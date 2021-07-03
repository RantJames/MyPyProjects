# length and width can be taken from user
width = 7
length = 21
patt = '.|..|.'
new_patt = '.|.'
for i in range(1, round(width/2)):
    print(new_patt.center(length, '-'))
    new_patt += str(patt)
print('WELCOME'.center(length, '-'))
for i in range(0, round(width/2)-1):
    rev_patt = new_patt[i*6+6:]
    print(rev_patt.center(length, '-'))

