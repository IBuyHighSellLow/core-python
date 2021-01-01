'''
catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or press nothing to stop.):')
    name =input()
    if name == '':
        break
    catNames=catNames + [name]
print('The cat names are:')
for name in catNames:
    print(' '+ name)
'''
'''
myPets = ['zophie', 'pooka', 'fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named '+ name)
else:
    print(name + ' is my pet.')

    '''
'''
You can consider random.choice(someList) to be a shorter form of someList[random.randint(0, len(someList) – 1] 
'''

'''
name = 'palabra'

for i in name:
    print('***' + i + '*** LALALA')
    '''

#CONWAYS GAME

import random, time, copy 
width = 60
height = 20

#create a list of list for cells

nextCells = []
for x in range(width):
    column=[] #create a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')# add a living cell
        else:
            column.append('')# add a dead cell
        nextCells.append(column) #nextCells is a list of column lists

    while True: #Main program loop
        print('\n\n\n\n\n') #separete each step with newlines
        currentCells= copy.deepcopy(nextCells)

        #print currentCells on the screen:
        for y in range(height):
            for x in range(width):
            print(currentCells[x][y], end='') # print the # or space
        print() #print a newline at the end of the row

        #calculate the next steps cells based on current step cells

        for x in range(width):
            for y in range(height):
                #get neighboring coordinates:
                leftCoord = (x-1) % width
                rightCoord = (x +1) % width
                aboveCoord = (y-1) % width
                belowCoord = (y+1) % height


                #count if number of living neighbors:
                numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

                            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
                numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.