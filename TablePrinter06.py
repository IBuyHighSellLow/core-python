tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colwidths=[0]*len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j])>colwidths[i]:
                colwidths[i]=len(table[i][j])


    for line in range(len(table[0])): #PYTHON PRINTS LINE PER LINE. NOT COLUMN PER COLUMN.ABOUT TABLE[0]: IT IS ESTABLISHED THAT ALL ITEMS IN TABLEDATA WILL HVE THE SAME LENGTH, SO THAT IT DOESNT MATTER WETHER YOU PUT [0], [1] OR [2] BECAUSE THEY ALL HAVE LENGTH OF 4 ITEMS (IN CASE OF THE TABLEDATA LIST
        for column in range(len(table)): #THERE ARE AS MANY COLUMNS AS ITEMS(LISTS) IN TABLEDATA
            print(table[column][line].ljust(colwidths[column]*2),end=" ") #NOW, WE PRINT THE FIRST WORD OF THE FIRST COLUMN, FOLLOWED BY THE FIRST WORD OF THE SECOND COLUMN AND SO ON. .END= HELPS WITH NOT HAVING TO CONCATENATE THESE AND KEEPING ITEMS IN THE SAME LINE.
        print() #WITHOUT THIS PRINT (WHICH PRINTS A NEW LINE), ALL ITEMS WOULD BE IN THE SAME LINE, DUE TO THE PREVIOS .END=

    print(tableData[1][2])

printTable(tableData)
