'''
Mingzhe Li (ml1252) Chaoqin Chen (cc1504) Guantao Zhao (gz87)
'''

import pickle
import cell
import repeatedForwardAStar
import repeatedBackwardAStar
import repeatedAdaptiveAStar

import time

#101x101 Map
s = 'Map50'

#5x5 Map for test
#s = '5x5Map'

#10x10 Map for test
#s = '10x10Map'

f = open(s, 'rb+')
g = pickle.load(f)
f.close() 

# For 101x101
start = cell.cell(10,4)
goal = cell.cell(75,90)

#For 5x5 
#start = cell.cell(0,1)
#goal = cell.cell(0,4)

#For 10x10
#start = cell.cell(6,4)
#goal = cell.cell(2,7)


t0 = time.time()
path=[]

#Forward A Star
path,expCells = repeatedForwardAStar.repeatedAStar(g, start, goal)
print "Using Forward A Star"

#Backward A Star--Takes long time in 101x101(Use for 5x5 or 10x10 Maps)
#path,expCells = repeatedBackwardAStar.repeatedAStar(g, start, goal)
#print "Using Backward A Star"

#Adaptive A Star
#path,expCells = repeatedAdaptiveAStar.repeatedAStar(g, start, goal)
#print "Using Adaptive A Star"
t1 = time.time()

if(path):
    path = [(start.row,start.column)] + path
print 'Time taken : %f' %(t1-t0),' Expanded Cells : %f' %(expCells) 
if(not path):
    print  'No path',' Time taken : %f' %(t1-t0),' Expanded Cells : %f' %(expCells) 

g.printGrid((start.row,start.column),(goal.row,goal.column),path)