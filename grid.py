
import cell
import pygame
import random

class grid(object):
    
    def __init__(self,size,width,height,margin):
        """
        Return a grid object with initial values.
        """ 
        
        self.Matrix = []
        for row in range(size):
            # Add an empty array that will hold each cell
            # in this row
            self.Matrix.append([])
            for column in range(size):
                self.Matrix[row].append(cell.cell(row,column))  # Append a cell

        self.size = size
        self.width=width
        self.height=height
        self.margin=margin
    
    def getCell(self,r,c):
       
        return self.Matrix[r][c]  

    def printGrid(self,start=(),goal=(),path=[]):
            
         
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREY = (50,50,50)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0,0,255)
        YELLOW = (255,255,0)
 
        # This sets the WIDTH and HEIGHT of each grid location
        WIDTH = self.width
        HEIGHT = self.height
 
        # This sets the margin between each cell
        MARGIN = self.margin
 
        #List to hold the traveled path
        travPath = []
 
        GRID_SIZE = self.size
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = []
        for row in range(GRID_SIZE):
            # Add an empty array that will hold each cell
            # in this row
            grid.append([])
            for column in range(GRID_SIZE):
                if(self.Matrix[row][column].isBlocked()):
                    grid[row].append(1)  # Append a cell
                else:
                    grid[row].append(0)  # Append a cell
 
        # Set row 1, cell 5 to one. (Remember rows and
        # column numbers start at zero.)
        #grid[2][5] = 1
        
        # Loop until the user clicks the close button.
        done = False
 
        # Initialize pygame
        pygame.init()
        
        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [GRID_SIZE*(WIDTH+MARGIN)+MARGIN , GRID_SIZE*(HEIGHT+MARGIN)+MARGIN ]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        
        #Display Title
        pygame.display.set_caption("Maze")
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
 
        
        
            screen.fill(BLACK)
        
            # Draw the grid
            for row in range(GRID_SIZE):
                for column in range(GRID_SIZE):
                    color = WHITE
                    if grid[row][column] == 1:
                        color = GREY
                    #Display the tarveled path
                    if((row,column) in travPath):
                        color = RED
                    if((row,column) == start):
                        color = BLUE
                    if((row,column) == goal):
                        color=YELLOW
                    
                    pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            if(path):
                (pathrow,pathcol) = path.pop(0)
                travPath.append((pathrow,pathcol))
                pygame.draw.rect(screen,
                                 GREEN,
                                 [(MARGIN + WIDTH) * pathcol + MARGIN,
                                  (MARGIN + HEIGHT) * pathrow + MARGIN,
                                  WIDTH,
                         HEIGHT])
            
            
            pygame.display.flip()
            
            # Limit to 10 frames per second
            clock.tick(10)
 
        # Be IDLE friendly.
        # on exit.
        pygame.quit()

    def left(self,cell):
        """
        Returns the left neighbor of the cell
        """
        if(cell.column >= 1):
            return self.getCell(cell.row,cell.column-1)
        else:
            return None
    
    def right(self,cell):
        """
        Returns the right neighbor of the cell
        """
        if(cell.column < self.size-1):
            return self.getCell(cell.row,cell.column+1)
        else:
            return None
    
    def up(self,cell):
        """
        Returns the upper neighbor of the cell
        """
        if(cell.row >= 1):
            return self.getCell(cell.row-1,cell.column)
        else:
            return None
    
    def down(self,cell):
        """
        Returns the lower neighbor of the cell
        """
        if(cell.row < self.size-1):
            return self.getCell(cell.row+1,cell.column)
        else:
            return None

    def generate(self):
        """
        Generates the grid using DFS
        """
        visited = []
        
        #Change this to arbitrary
        nodes_stack = [self.getCell(2,2)]
        
        # Intialize visited with zeroes  
        for row in range(self.size):
            # Add an empty array that will hold each cell
            # in this row
            visited.append([])
            for column in range(self.size):
                visited[row].append(0)  # Append a cell
                   
    
        #Traversal
        while nodes_stack:
            curNode = nodes_stack.pop()
            
            #Probability of 70% being unblocked 
            if(random.randint(0,99) >= 70):
                curNode.setBlocked(True)
            
            #set visited to True    
            visited[curNode.row][curNode.column] = 1
            
            #Add neighbors to stack
            if(self.left(curNode)):
                if(not visited[curNode.row][curNode.column-1]):
                    nodes_stack.append(self.left(curNode))
                    visited[curNode.row][curNode.column-1] = 1
            if(self.right(curNode)):
                if(not visited[curNode.row][curNode.column+1]):
                    nodes_stack.append(self.right(curNode))
                    visited[curNode.row][curNode.column+1] = 1
            if(self.up(curNode)):
                if(not visited[curNode.row-1][curNode.column]):
                    nodes_stack.append(self.up(curNode))
                    visited[curNode.row-1][curNode.column] = 1
            if(self.down(curNode)):
                if(not visited[curNode.row+1][curNode.column]):
                    nodes_stack.append(self.down(curNode))
                    visited[curNode.row+1][curNode.column] = 1
    
    def neighbors(self,cell):
        """
        Returns the adjacent neighbors as a list
        """
        neighbors = []
        
        if(self.up(cell)):
            neighbors.append(self.up(cell))
        if(self.right(cell)):
            neighbors.append(self.right(cell))
        if(self.down(cell)):
            neighbors.append(self.down(cell))
        if(self.left(cell)):
            neighbors.append(self.left(cell))
            
        return neighbors