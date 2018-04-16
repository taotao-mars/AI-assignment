

import heapq

class PriorityQueue:
    
   # This is the implementation of a binary heap using heapq library
    
    #Attributes:
    #elements: The list of elements in the heap
   
    def __init__(self):
        self.elements = []
    
    def empty(self):
        """
        Returns true if the queue is empty
        """
        return len(self.elements) == 0
    
    def put(self, item, priority):
        """
        Inserts the item with priority
        """
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        """
        Returns the topmost element from the queue
        """
        return heapq.heappop(self.elements)[1]
