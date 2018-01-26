names = ['Bob', 'Sinon', 'Asuna', 'Silica', 'Kirito']
def list1000(a):
    NN = input('Add a new name! ')
    a.append(NN)
    AN = input('Do you want to add another name (y/n)? ')
    if AN == 'y' or AN == 'Y':
        list1000(a)
    else:
        print ('')
    return a

print(list1000(names))
