# App to demonstrate NearestNeighbor queries in action
import Tkinter
from kdtree import *

class KDTreeApp:
    def __init__(self):
        """App for creating KD tree dynamically"""
        
        self.tree = KDTree()
        self.match = None
        self.redraw = False
        self.shortline = None
        
        self.master = Tkinter.Tk()
        self.w = Tkinter.Frame(self.master, width=410, height=410)
        self.canvas = Tkinter.Canvas(self.w, width=400, height=400)        
                        
        self.paint()

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<Motion>", self.moved)
        self.w.pack()
        self.w.mainloop()

    def toCartesian(self, y):
        return self.w.winfo_height() - y

    def toTk(self,y):
        if y == maxValue: return 0
        tk_y = self.w.winfo_height()
        if y != minValue:
            tk_y -= y
        return tk_y

    def view(self):
        """Show window with points"""

    def moved(self, event):
        """React to mouse move events"""
        p = (event.x, self.toCartesian(event.y))

        match = self.tree.find(p)
        if match:
            self.redraw = True
            p = match.point
            self.canvas.create_rectangle(p[X_] - 4, self.toTk(p[Y_]) - 4, p[X_] + 4, self.toTk(p[Y_]) + 4, fill='Red')
            self.canvas.delete(self.shortline)
            self.shortline = None
        else:
          if self.redraw:
              self.paint()
              self.redraw = False
          n = self.tree.nearest(p)
          if n:
              pn = n.point
              if self.shortline is None:
                  self.shortline = self.canvas.create_line(pn[X_], self.toTk(pn[Y_]), p[X_], self.toTk(p[Y_]), tags="shortline")
              else:
                  self.canvas.coords("shortline", pn[X_], self.toTk(pn[Y_]), p[X_], self.toTk(p[Y_]))
         
          
    def click(self, event):
        """Add point to KDtree"""
        p = (event.x, self.toCartesian(event.y))
        
        self.tree.add(p)
        if self.shortline:
            self.canvas.delete(self.shortline)
            self.shortline = None
            
        self.paint()

    def drawPartition (self, r, p, orient):
        if orient == VERTICAL:
            self.canvas.create_line(p[X_], self.toTk(r.y_min), p[X_], self.toTk(r.y_max))
        else:
            xlow = r.x_min
            if r.x_min == minValue: xlow = 0
            xhigh = r.x_max
            if r.x_max == maxValue: xhigh = self.w.winfo_width()

            self.canvas.create_line(xlow, self.toTk(p[Y_]), xhigh, self.toTk(p[Y_]))

        self.canvas.create_rectangle(p[X_] - 4, self.toTk(p[Y_]) - 4, p[X_] + 4, self.toTk(p[Y_]) + 4, fill='Black')

    def visit (self, n):
        if n == None: return

        self.drawPartition(n.region, n.point, n.orient)

        self.visit (n.below)
        self.visit (n.above)

    def prepare(self, event):
        """prepare to add points"""
        if self.label:
            self.label.destroy()
            self.label = None
            self.canvas.pack()
        
    def paint(self):
        if self.tree.root:
            for child in self.canvas.winfo_children():
                child.destroy()
            self.visit(self.tree.root)
        else:
            self.label = Tkinter.Label(self.w, width=100, height = 40, text="Click To Add Points")
            self.label.bind("<Button-1>", self.prepare)
            self.label.pack()
            
      
if __name__ == "__main__":
    KDTreeApp()

"""
Change Log

1. 2014.05.23     import changed to use KDTree from kdtree.py file

 
"""
