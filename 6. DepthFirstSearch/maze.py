# Maze construction using DepthFirstSearch Traversal

import random
import numpy
import Tkinter
import sys

White = 0
Gray = 1
Black = 2

class Maze:

    def __init__(self, height, width, size):
        """initialize maze"""
        if size < 3:
            raise Exception ("Cells must be at least three pixels wide")
        self.height = height
        self.width = width
        self.size = size
        self.numrows = height/size
        self.numcols = width/size
        self.construct()

    def view(self):
        """Show window with maze"""
        
        master = Tkinter.Tk()
        w = Tkinter.Canvas(master, width=self.width+10, height=self.height+10)
        w.pack()
        offset = 5
        w.create_line(offset, offset, offset, offset+self.height)
        w.create_line(offset, offset, offset + (self.width/self.size/2)*self.size, offset)
        w.create_line(offset + self.size*(1+(self.width/self.size)/2), offset, \
                      offset + (self.width/self.size)*self.size, offset)
        
        for r in range(self.numrows):
            for c in range(self.numcols):
                if self.hasSouthWall[r,c]:
                    w.create_line(offset + c*self.size, offset + (r+1)*self.size, \
                                  offset + (c+1)*self.size, offset + (r+1)*self.size)
                if self.hasEastWall[r,c]:
                    w.create_line(offset + (c+1)*self.size, offset + r*self.size, \
                                  offset + (c+1)*self.size, offset + (r+1)*self.size)
        Tkinter.mainloop()

     
    def clearWall(self, fromCell, toCell):
        """Remove wall between two cells"""
        if fromCell[1] == toCell[1]:
          self.hasSouthWall[min(fromCell[0],toCell[0]),fromCell[1]] = False
        else:
          self.hasEastWall[fromCell[0], min(fromCell[1], toCell[1])] = False

    def dfsVisit(self, sq):
        """conduct DFS search to build maze"""
        self.color[sq] = Gray
        
        while len(self.neighbors[sq]) > 0:
            cell = random.choice(self.neighbors[sq])
            self.neighbors[sq].remove(cell)
            if self.color[cell] == White:
                self.clearWall(sq, cell)
                self.dfsVisit(cell)
                
        self.color[sq] = Black

    def dfsVisit_nr(self, sq):
        """conduct non-recursive DFS search to build maze"""
        path = [sq]
        self.color[sq] = Gray

        while len(path) > 0:
            sq = path[0]
            more = self.neighbors[sq]
            if len(more) > 0:
                cell = random.choice(self.neighbors[sq])
                self.neighbors[sq].remove(cell)
                if self.color[cell] == White:
                    self.clearWall(sq, cell)
                    path.insert(0, cell)
                    self.color[cell] = Gray
            else:
                self.color[sq] = Black
                del path[0]
    


    def construct(self):
        """construct maze of given height/width and size"""

        self.color = dict( ((r,c),White) \
                   for r in range(self.numrows) \
                   for c in range(self.numcols) )

        self.hasEastWall = dict( ((r,c),False) \
                   for r in range(self.numrows) \
                   for c in range(self.numcols) )
        
        self.hasSouthWall = dict( ((r,c),False) \
                   for r in range(self.numrows) \
                   for c in range(self.numcols) )
        
        self.neighbors = dict( ((r,c),[]) \
                   for r in range(self.numrows) \
                   for c in range(self.numcols) )

        for r in range(self.numrows):
            for c in range(self.numcols):
                n = self.numcols*r + c
                self.hasEastWall[r,c] = True
                self.hasSouthWall[r,c] = True
                
                if r != 0:
                   self.neighbors[r,c].append((r-1,c))
                if r != self.numrows-1:
                   self.neighbors[r,c].append((r+1,c))
                
                if c != 0:
                   self.neighbors[r,c].append((r,c-1))
                if c != self.numcols-1:
                   self.neighbors[r,c].append((r,c+1))

        sq = (0, self.numcols/2)
        self.dfsVisit_nr(sq)
        
        self.hasSouthWall[self.numrows-1,self.numcols/2] = False
    
if __name__ == "__main__":
    m = Maze(400, 400, 10)
    m.view()

"""
Change Log

1. 2014.05.23    Added default execution on __main__ to show sample maze

"""

