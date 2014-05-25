# BinaryHeap implementation (with decreaseKey operation)

# Each element is a list of two elements (priority, element)   
PRIORITY = 0
ID = 1

# data structure. Start by describing the priority queue as storing
# identifiers (drawn from set [0, n-1]) and an associated integer priority
# where lower values imply greater importance

class BHeap:

    def __init__(self, size):
        """initialize Binary Heap to given number of elements"""
        self.size      = size
        self.n         = 0
        self.elements  = [[0, None] for i in range(size+1)]
        self.positions = [0 for i in range(size+1)]

    def isEmpty(self):
        """Determine whether Binary Heap is empty"""
        return self.n == 0

    def smallest(self):
        """Extract and return smallest element in heap"""
        id = self.elements[1][ID]
        
        # heap will have one less entry, so place final one appropriately
        last = self.elements[self.n]
        self.n -= 1

        self.elements[1] = last
        pIdx = 1
        child = pIdx * 2
        while child <= self.n:
            # select smaller of two children
            sm = self.elements[child]
            if child < self.n:
                if sm[PRIORITY] > self.elements[child+1][PRIORITY]:
                    child += 1
                    sm = self.elements[child]

            if last[PRIORITY] <= sm[PRIORITY]:
                break

            self.elements[pIdx] = sm
            self.positions[sm[ID]] = pIdx

            pIdx = child
            child = 2*pIdx

        self.elements[pIdx] = last
        self.positions[last[ID]] = pIdx
        return id
    

    def insert(self, id, priority):
        """Insert item into heap with given priority"""
        self.n += 1
        i = self.n
        while i > 1:
            pIdx = int(i/2)
            p = self.elements[pIdx]

            if priority > p[PRIORITY]:
                break

            self.elements[i] = p
            self.positions[p[ID]] = i
            i = pIdx

        self.elements[i] = [priority, id]
        self.positions[id] = i
        
    def decreaseKey(self, id, newPriority):
        """Reduce the priority for the given item"""

        size = self.n
        self.n = self.positions[id] - 1

        self.insert(id, newPriority)

        self.n = size


"""
Change Log

1. 2014.05.24    insert()
                 defect: allocate storage on insert otherwise insert
                         after deletion causes duplicate references.
                 fix:    self.elements[i] = [priority, id]
"""
