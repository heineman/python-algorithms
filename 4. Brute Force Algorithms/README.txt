Module 4 Brute Force Algorithms

This module contains the following files

  * bruteForce.py implements algorithm for solving combinatoric problems
  * project_bruteForce.py implements magicSquare implementation

To evaluate the bruteForce algorithm create a peg solitaire game as follows:

  >>> board = initial(5, (4,2))

This will create a 5x5 peg solitaire game (with 15 holes) and place a peg in
every hole except for (4,2) which is the hole two rows below the topmost peg.
Note that the video lecture (and slides) explains the numbering scheme for 
the pegs. For the 5x5 peg solitaire game, its numbering is as follows:

 
                    (4,4)

                (3,3)   (5,3)
     
            (2,2)   (4,2)   (6,2)

        (1,1)   (3,1)   (5,1)   (7,1)

    (0,0)   (2,0)   (4,0)   (6,0)   (8,0)


Solve this puzzle by calling following function:

  >>> solveSpecific(board)

The moves that form the solution will be printed. The final remaining peg will
be left in the middle hole (4,0) of the board.

Other solvable configurations are possible (such as starting with (4,4) as empty).

The Magic Square problems are found in project_bruteForce.py and can be run as follows:

   >>> initialize(3)
   >>> solve(3)
   True
   >>> output()
   2  7  6
   9  5  1
   4  3  8

You can try on a 4x4 board but it will take significantly longer to complete. 
instead of waiting for a 'solve(4)' invocation to run, run the modified
'solveit(4)' 

   >>> initialize(4)
   >>> solveit(4)
   True
   >>> output()
    1  2 15 16
   12 14  3  5
   13  7 10  4
    8 11  6  9

