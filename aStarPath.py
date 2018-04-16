

import priorityQueue

def heuristic(a, b):
    """
    This function provides the Manhattan distance between the cells a and b
    """
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(Came_From,current):
    """
    This function provides the best path for reaching goal
    """
    
    total_path = [current]
    while current in Came_From.keys():
        current = Came_From[current]
        total_path.append(current)
    return total_path

def aStar(grid,start,goal):
    """
    A* Algorithm implementation
    """
    
    #Inititalize values 
    closedSet = []
    openSet = priorityQueue.PriorityQueue()
    openSet.put((start.row,start.column),0)
    cameFrom = {}
    totExpandedCells = 0;    
    
    g_score = {}
    g_score[(start.row,start.column)] = 0
    f_score = {}
    f_score[(start.row,start.column)] = heuristic((start.row,start.column), (goal.row,goal.column))
    
    while not openSet.empty():
        
        #Take the lowest f-value element from the openSet
        (current_row,current_column) = openSet.get()
        totExpandedCells = totExpandedCells + 1  #Required for analysis of algorithm
        
        #If this is the goal state, return path
        if current_row == goal.row and current_column == goal.column :
            return reconstruct_path(cameFrom, (goal.row,goal.column)),totExpandedCells
        
        closedSet.append((current_row,current_column))
        for neighbor in grid.neighbors(grid.getCell(current_row,current_column)):
            #Ignore cell if blocked
            if grid.getCell(neighbor.row,neighbor.column).isBlocked():
                continue
            
            #Compute tentative g score
            tentative_g_score = g_score[(current_row,current_column)] + heuristic((neighbor.row,neighbor.column),(current_row,current_column))
            
            
            #if not the best path to this node -- Check closed List
            if (neighbor.row,neighbor.column) in closedSet and tentative_g_score > g_score.get((neighbor.row,neighbor.column),0):
                continue

            #If the most promised path to the node -- Check openList
            if tentative_g_score < g_score.get((neighbor.row,neighbor.column),0) or (neighbor.row,neighbor.column) not in [i[1]for i in openSet.elements]:
            #This is the best path till now. Record it!!!
                cameFrom[(neighbor.row,neighbor.column)] = (current_row,current_column)
                g_score[(neighbor.row,neighbor.column)] = tentative_g_score
                f_score[(neighbor.row,neighbor.column)] = g_score[(neighbor.row,neighbor.column)] + heuristic((neighbor.row,neighbor.column),(goal.row,goal.column))
                
                #Tie breaking with bigger g
                openSet.put((neighbor.row,neighbor.column), 10000*f_score[(neighbor.row,neighbor.column)] - (tentative_g_score))
                
                #Tie breaking with smaller g
                #openSet.put((neighbor.row,neighbor.column), 10000*f_score[(neighbor.row,neighbor.column)] + (tentative_g_score))
            
    return None,totExpandedCells
    
                
        
        
