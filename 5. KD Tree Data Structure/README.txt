Module 5 KD Tree 

This module contains the KD Tree implementation as developed in this module.
Because the project required changes to the data structure, I have updated
the kdtree.py file to contain all necessary functionality.

Files contained within this module include:

  * kdtree.py    Implements KDtree and supports nearest neighbor query
  * app.py       App for demonstrating construction of KD tree graphically
  * app_nn.py    App that demonstrates nearest neighbor query to current cursor
                 while the KD tree is being constructed

The applications are self-launching. Simply load each one in Idle and execute.

When reviewing the code you may be surprised to see that the nearest() function may
execute two recursive calls. This happens if the logic determines that the nearest
point might be in either of the above or below child trees, and it can't conclusively
determine without checking both. This happens when the perpendicular distance (to the 
axis along which the node partitions the plane) is in fact smaller than the current
mind distance being passed in the recursion. When this happens, it is possible that 
the minimum distance point is in either partition, so the code must check both.

Change Log

1. 2014.05.23	KDNode:nearest() function
                defect: in double recursion case, was comparing
                        distance to self.above (and self.below)
                        instead of the returned point pt.

2. 2014.05.23   changes name of import in app_nn.py to reflect kdtree.py
