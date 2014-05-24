# Mathematical algorithms project
import random

largePrime = 622288097498926496141095869268883999563096063592498055290461

def isPrime(n, k=5):
    """Probabilistically check whether number is prime"""
    
    for i in range(k):
        a = random.randint(1,n-1)
        val = pow (a, n-1, n)
        if val != 1:
            return False
    
    return True
