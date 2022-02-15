#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

A = 0
numLength = len(Belgium)


while A < numLength:
    # print('-')

    A += 1


newList = Belgium.replace(',', ': ')


def convert(string):
    li = list(string.split(":"))
    return li


totalPopList = convert(newList)
print(totalPopList)

totalPop = int(totalPopList[1]) + int(totalPopList[3])
print(totalPop)




