"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""

import multiprocessing as mp

def is_multiple_of_three_or_five(x):
    if x % 3 == 0 or x % 5 == 0:
        return x
    
    return 0

def solve():
    pool = mp.Pool(processes=mp.cpu_count())
    result = pool.starmap(is_multiple_of_three_or_five, [[1, 2, 3, 4, 5], [6, 7, 8, 9, ]])
    return sum(result)
