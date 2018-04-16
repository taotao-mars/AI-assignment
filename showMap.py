
import grid
import pickle

str = '10x10Map'

f = open(str, 'rb+')
g = pickle.load(f)
f.close()

g.printGrid()
