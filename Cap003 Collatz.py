def collatz(number):
    """ check if the number is even or odd and performs calculations.
    """
    if number % 2  == 0: # even
        print(number // 2)
        return number //2
    elif number % 2 != 0: # odd 
        result = 3*number+1
        print(result)
        return result

try:
    n = int(input('Enter number: ')) # takes user input
    while n !=1 and n > 1: # performs while loop until 'n' becomes 1
        n = collatz(int(n)) # passes 'n' to collatz() function until it arrives at '1'
except ValueError:
    print('Value Error. Please enter integer.')


''' segunda solucion

def collatz(number):
    while True:
        if number <= 1:
            break
        elif number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print (number)
try:
    print('Enter a number \n')
    number = int(input())
    collatz(number)
except ValueError:
    print('Invalid value, Enter a number.')

'''
