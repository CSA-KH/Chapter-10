def mylistapp():
    myList = []
    myList.append(76)
    myList.append(92.3)
    myList.append('hello')
    myList.append(True)
    myList.append(4)
    myList.append(76)
    print (myList)


def mylistcon():
    mylist = []
    mylist += [76]
    mylist += [92.3]
    mylist += ['hello']
    mylist += [True]
    mylist += [4]
    mylist += [76]
    print (mylist)


def avarage():
    import random
    tot = 0
    num = []
    for x in range(1000):
        rand = random.randrange(1,1001)
        num.append(rand)
    for i in num:
        tot += i
    print (tot/100)


mylistapp()
print ('\n')
mylistcon()
print ('\n')
avarage()

