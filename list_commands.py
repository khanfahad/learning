N = int(input("number of commands? ")) # number of commands to input
myList = []
while True:
    if N == 0:
        break
    comm = input("command?").split() # split input into list
    if str(comm[0]) == 'insert':
        myList.insert(int(comm[1]), comm[2]) # if 'insert' put first integer in position by second
    elif str(comm[0]) == 'print':
        print(myList)
    elif str(comm[0]) == 'remove':
        myList.remove(comm[1])
    elif str(comm[0]) == 'append':
        myList.append(comm[1])
    elif str(comm[0]) == 'sort':
        myList = sorted(myList)
    elif str(comm[0]) == 'pop':
        myList.pop()
    elif str(comm[0]) == 'reverse':
        myList.reverse()
    N -= 1
