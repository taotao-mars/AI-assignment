
import aStarPath
import grid

def repeatedAStar(origMap,start,goal):
    
    
    agentMap = grid.grid(origMap.size,origMap.width,origMap.height,origMap.margin)
    agentPos = start
    path = []
    expandedCells = 0
    
    while not (agentPos.row == goal.row and agentPos.column == goal.column):
           
            #Update map           
            for neighbor in origMap.neighbors(agentPos):
                if(neighbor.isBlocked()):
                    agentMap.getCell(neighbor.row, neighbor.column).setBlocked(True)

            #Calculate best path as per available input
            bestPath,aStarExpandedCells = aStarPath.aStar(agentMap, agentPos, goal)
            expandedCells = expandedCells + aStarExpandedCells
            
            #If no path is available
            if(not bestPath):
                return None,expandedCells
            
            #Traverse 1 step in the direction
            l = len(bestPath)-2
            (pathStepX,pathStepY) = bestPath[l]
            agentPos = origMap.getCell(pathStepX,pathStepY)
            
            #recordPath
            path.append(bestPath[l])
            
    return path,expandedCells