# Kd Tree Implementation With Nearest Neighbor Functionality

maxValue = 2147483647
minValue = -2147483648

HORIZONTAL = 0
VERTICAL   = 1

X_ = 0
Y_ = 1

class Region:
    """Represents region in Cartesian space"""

    def __init__(self, xmin,ymin, xmax,ymax):
        """Creates region from (xmin,ymin) to (xmax,ymax)"""

        self.x_min = xmin
        self.y_min = ymin
        self.x_max = xmax
        self.y_max = ymax

    def copy(self):
        """Return copy of region"""
        return Region(self.x_min, self.y_min, self.x_max, self.y_max)

# default maximum region
maxRegion = Region(minValue, minValue, maxValue, maxValue)

class KDNode:

    def __init__(self, pt, orient, region = maxRegion):
        """Create empty KDNode"""
        self.point  = pt
        self.orient = orient
        self.above  = None
        self.below  = None
        self.region = region

    def createChild(self, pt, below):
        """Create child node (either above or below) given node with pt"""

        r = self.region.copy()
        if self.orient == VERTICAL:
            if below:
                r.x_max = self.point[X_]
            else:
                r.x_min = self.point[X_]
        else:
            if below:
                r.y_max = self.point[Y_]
            else:
                r.y_min = self.point[Y_]

        return KDNode(pt, 1-self.orient, r)

    def distance(self, pt):
        """Compute distance from self to pt"""
        if pt:
            return ((self.point[X_] - pt[X_])**2 + (self.point[Y_] - pt[Y_])**2) ** 0.5

    def isBelow(self, pt):
        """Is point below current node"""
        if self.orient == VERTICAL:
            return pt[X_] < self.point[X_]
        return pt[Y_] < self.point[Y_]

    def isAbove(self, p):
        """Determine if point is below partitioning line"""
        if self.orient == VERTICAL:
            return p[X_] >= self.point[X_]
        return p[Y_] >= self.point[Y_]

    def add(self, pt):
        """Add point to the KDNode tree rooted at this node"""

        if self.point == pt:
            return

        if self.isBelow(pt):
            if self.below:
                self.below.add(pt)
            else:
                self.below = self.createChild(pt, True)
        else:
            if self.above:
                self.above.add(pt)
            else:
                self.above = self.createChild(pt, False)

    def nearest(self, mind, p):
        """Return closest node from given subtree to point."""
        d = self.distance(p)
        result = None
        if (d < mind):
            result = self
            mind = d
            
        if self.orient == VERTICAL:
            dp = abs(self.point[X_] - p[X_])
        else:
            dp = abs(self.point[Y_] - p[Y_])

        if dp < mind:
            if self.above:
                pt = self.above.nearest(mind, p)
                if pt:
                    md = pt.distance(p)
                    if md < mind:
                        result = pt
                        mind = md
            if self.below:
                pt = self.below.nearest(mind,p)
                if pt:
                    md = pt.distance(p)
                    if md < mind:
                        result = pt
                        mind = md
        else:
            pt = None
            if self.isAbove(p) and self.above:
                pt = self.above.nearest(mind, p)
            elif self.isBelow(p) and self.below:
                pt = self.below.nearest(mind, p)
            if pt:
                return pt

        return result


class KDTree:

    def __init__(self):
        """Create empty KD Tree"""
        self.root = None

    def add(self, pt):
        """Add Point to KD-tree"""

        if self.root:
            self.root.add(pt)
        else:
            self.root = KDNode(pt, VERTICAL)
            

    def find(self,p):
        """Find point in KD tree within 5 units"""

        n = self.root
        while n:
            if n.distance(p) < 5:
                return n

            if n.isBelow(p):
                n = n.below
            else:
                n = n.above
    
        return n

    def nearest(self,p):
        """Return closest node in KD tree to given point"""

        if self.root is None: return None
        
        # find node which would have been parent of point
        n = self.root
        while n.point != p:
            if n.isBelow(p):
                if n.below:
                    n = n.below
                else:
                    break
            else:
                if n.above:
                    n = n.above
                else:
                    break

        
        mind = n.distance(p)
        better = self.root.nearest(mind, p)
        if better:
           return better
        return n

"""
Change Log

1. 2014.05.23    KDNode:nearest() function
                 defect: in double recursion case, was comparing
                         distance to self.above (and self.below)
                         instead of the returned point pt.

"""
