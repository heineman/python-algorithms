# magic square construction

board = []
used = []
magicSum = [0]

def initialize(n):
    """prepare board"""
    del board[0:len(board)]
    del used[0:len(used)]
    for r in xrange(n):
        board.append ([0 for c in xrange(n)])
    for d in range(n*n+1):
        used.append(False)
    magicSum[0] = n*(n*n+1)/2

def output():
    """Output board"""
    for row in board:
        for val in row:
            print ("{:2d}".format(val)),
        print

def isValid(n):
    """Determine if board is valid"""
    
    sumD1 = sumD2 = 0
    for i in range(n):
      sumR = sumC = 0
      
      sumD1 += board[i][i]
      sumD2 += board[i][n-i-1]

      for j in range(n):
        sumR += board[i][j]
        sumC += board[j][i]

      if sumR != magicSum[0] or sumC != magicSum[0]:
          return False

    return sumD1 == magicSum[0] and sumD2 == magicSum[0]

def solve(n, step=0):
    """Complete given step in magic square board"""
        
    if step == n**2:
        return isValid(n)

    for val in range(1,n**2+1):
        if not used[val]:
            
            used[val] = True
            board[step/n][step%n] = val
            if solve(n, step+1):
                return True

            board[step/n][step%n] = 0
            used[val] = False

    return False
                 
# Use this existing solution for 3x3 and it works great. Use for 4x4 and
# it takes several minutes to come back with the solution. This brute
# force technique is trying 16! = 20,922,789,888,000 possible solutions.
# This roughly is 5,765,760 times more work than solving the 3x3. Can we
# find a way to do better? YES!
# Instead of blindly pursuing each recursive step, you can validate partial
# results before moving forward.
# revise as shown:

def validUpTo(n,step):
    """Determine if valid so far. Rewritten to take advantage of fact that
    you don't need to check each row/col up to step, but only the row or
    column at step. Improves performance by about 50%"""
    if step % n == n-1:
        r = (step + 1 - n)/n
        if sum(board[r]) != magicSum[0]:
            return False

    if step >= n*n-n:
        c = step % n
        total = 0
        for r in range(n):
            total += board[r][c]
        if total != magicSum[0]:
            return False

    return True

def solveit(n, step=0):
    """Complete given step in magic square board"""
    
    if step == n**2:
        return isValid(n)

    for val in range(1,n**2+1):
        if not used[val]:
            
            used[val] = True
            board[step/n][step%n] = val
            if validUpTo(n,step) and solveit(n, step+1):
                return True

            board[step/n][step%n] = 0
            used[val] = False

    return False
                 
# Note that these solutions won't work for 5x5. If you let the following
# code run for several hours, it will report there are 7040 squares.

def up2():
    from time import time
    now = time()
    num = [0]
    count(4, 0, num)
    print num, " solutions"
    print time() - now

def count(n, step=0, number=[0]):
    """Count number of solutions and return as first element in number."""
        
    if step == n**2:
        if isValid(n):
            number[0] += 1
        return

    for val in range(1,n**2+1):
        if not used[val]:
            
            used[val] = True
            board[step/n][step%n] = val
            if validUpTo(n,step):
                count(n, step+1, number)

            board[step/n][step%n] = 0
            used[val] = False

