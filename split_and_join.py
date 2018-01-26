def split_and_join():
    s = ('My name is Jose')
    s = s.split()  #splits by the space inbetween words.
    print (s)
    u = ('user1;user2;user3')
    u = u.split(';')  #splits string at every ;
    print (u)
    sen = ['this', 'is', 'a', 'sentence']
    glue = (' ')
    a = glue.join(sen)  #joins the strings and puts a space inbetween the words
    print (a)

split_and_join()
