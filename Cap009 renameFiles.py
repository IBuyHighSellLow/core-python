#!python3

#renameDates.py - rename filenames with american mm-dd-yyyy date format 
#to european dd-mm-yyyy

import os


#Create a regex that matches files with the american date format

path = os.chdir('d:\\CCACO\\CCA TEMPLATE\\C001066 Sugar Creek\\Photos FGA')


i=0

for oldFileName in os.listdir(path):

    newFileName = 'Dpl {}.jpg'.format(i)

    os.rename(oldFileName, newFileName)

    i+=1
