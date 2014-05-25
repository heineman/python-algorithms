# min string edit distance dynamic programming example

def minEditDistance(s1, s2):
    """Compute minimum edit distance converting s1 -> s2"""

    m = {}
    len1 = len(s1)
    len2 = len(s2)
    maxlen = max(len1, len2)

    m = [None] * (len2 + 1)
    for i in range(len2+1):
        m[i] = [0] * (len1+1)

    # set up initial costs on horizontal
    for j in range(1, len1+1):
        m[0][j] = j

    # now prepare costs for vertical
    for i in range(1, len2+1):
        m[i][0] = i
    
    # compute best 
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            cost = 1
            if s1[j-1] == s2[i-1]: cost = 0

            # cost of changing [i][j] character
            # cost of removing character from sj
            # cost of adding character to si
            replaceCost = m[i-1][j-1] + cost
            removeCost  = m[i-1][j] + 1
            addCost     = m[i][j-1] + 1
            m[i][j]     = min(replaceCost,removeCost,addCost)

    return m[len2][len1]
