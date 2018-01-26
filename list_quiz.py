def list_quiz():
    names = ['Bob', 'Jenny', 'Steve', 'Alex', 'John']  #The names
    print (names)
    numbers = [24, 53, 32, 54, 63]  #The numbers
    print (numbers)
    both = [names + numbers]  #Adds both the name and the number
    print (both)
    names[3:3] = ['Afton', 'Peter']  #Adds the two names to names in the top
    print (names)

list_quiz()
