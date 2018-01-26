def list2():
    NBP = ['Keenan', 'Hui', 'April', '15', '2003', 'Freamont']
    for i in NBP:
        print (i)
    print ('\nI was born in %s.'%(NBP[5]))
    print ('\nThe month was %s.\n'%(NBP[2]))
    NBP [5:] = ['John', 'Rita']
    print (NBP)
list2()
