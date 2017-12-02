'''
Created on Nov 18, 2017

@author: ITAUser
'''
#open the text file
#read the file
#split the file
#count the letters
#print result

def lettercount(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True
    while run:
        letter = f.read(1) # 1 means read one character at a time
        # make the char lower case by using the function char.lower()
        letter = letter.lower()
        # if the character exists, note that if the 
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
    print(count)
lettercount("constituton.txt", "a")