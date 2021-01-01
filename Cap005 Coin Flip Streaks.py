import random
numberOfStreaks = 0
streak=0
for experimentNumber in range(100):
    # Code that creates a list of 100 'heads' or 'tails' values.
    
    coin_flip_100=[]
    for i in range(10):
        if random.choice([0, 1]) == True:  #Creating the random flip
            coin_flip_100.append(1)
        else:
            coin_flip_100.append(0)
        if i==0:
            pass
        elif coin_flip_100[i]== coin_flip_100[i-1]:
            streak+= 1  # checking pattern [1,1,1,1,1,1]
        else:
            streak=0
        if streak == 6:
            numberOfStreaks +=1

    print(coin_flip_100)
print('El patron se repitio: ' +str(numberOfStreaks) + ' veces')

print('Chance of streak: %s%%' % ((numberOfStreaks / (10*100))*100) )





'''
import random
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
print(randomlist)

'''

'''
for x in range(width):
    column=[] #create a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')# add a living cell
        else:
            column.append('')# add a dead cell
        nextCells.append(column) #nextCells is a list of column lists



    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))'''