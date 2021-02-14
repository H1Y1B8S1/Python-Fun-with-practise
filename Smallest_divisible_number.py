"""
python program to find the smallest number
evenly divisible by all number 1 to n.
"""

import math


def lcm(n):
    """Returns the lcm of first n numbers"""
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans * i) / math.gcd(ans, i))
    return ans


# main
n = 6
print(lcm(n))
