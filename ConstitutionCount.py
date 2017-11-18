'''
Created on Nov 4, 2017

@author: ITAUser
'''
#open the file
#read the file
#split the file
#print the number of words in the list

f = open('constituton.txt', 'r')
text = f.read()
words = text.split()
num_words = len(words)
print("There are " + str(num_words)+ " words in the constitution.")