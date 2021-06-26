# Menu driven program to perform operations on list


nlist = []


def list_ins(pos, ele):
    nlist.insert(pos, ele)


def list_app(ele):
    nlist.append(ele)


def list_remove(ele):
    nlist.remove(ele)


def list_sort():
    nlist.sort()


def list_reverse():
    nlist.reverse()


def list_pop():
    nlist.pop()


def list_print():
    print(nlist)


N = 2
for i in range(N):
    command = input().split()
    if command[0] == 'insert':
        list_ins(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        list_print()
    elif command[0] == 'remove':
        list_remove(int(command[1]))
    elif command[0] == 'append':
        list_app(int(command[1]))
    elif command[0] == 'sort':
        list_sort()
    elif command[0] == 'pop':
        list_pop()
    else:
        list_reverse()
