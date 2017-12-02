'''
Created on Dec 2, 2017

@author: ITAUser
'''
def calculate_char(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = False
    while not run:
        char = f.read(1)
        char = char.lower()
        if char == '':
            run = True
        if char == mychar:
                count = count + 1
    return count
import string
alphabet = list(string.ascii_lowercase)
numbers = []
for i in alphabet:
    icount = calculate_char('constituton.txt',i)
    numbers.append(icount)
maximum = max(numbers)
common = numbers.index(maximum)
print("The most common letter is " + alphabet[common] + ".")
print(maximum)