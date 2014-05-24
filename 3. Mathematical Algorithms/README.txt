Module 3 Mathematical Algorithms

This module contains the following files

  * mathematical.py

	This file implements ExponentiationBySquaring and Matrix Exponentiation

  * project_mathematical.py 

	Contains rapid primality test based on Fermat's little theorem

Change Log

1. 2014.05.23   mathematical.py (exponent_mat)
                defect: return x.dot(exponent (x.dot(x), (n-1)/2))
                fix:    return x.dot(exponent_mat (x.dot(x), (n-1)/2))

                defect: return exponent (x.dot(x), n/2)
                fix:    return exponent_mat (x.dot(x), n/2)

