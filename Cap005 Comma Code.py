'''def listTostring(someList):
    a = ''
    for i in range(len(someList)-1):
        a += str(someList[i])
    a += str('and ' + someList[len(someList)-1]
    print (a)

spam = ['apples', 'bananas', 'tofu', 'cats']
listTostring(spam)'''
import pyperclip

spam = ['apples','bananas', 'tofu', 'cats']



def some_list(fruits):
    for i in range(len(fruits) - 2):
        print(fruits[i], sep=', ', end=', ')
    print(fruits[-2] + ' and '+ fruits[-1])

some_list(spam)



