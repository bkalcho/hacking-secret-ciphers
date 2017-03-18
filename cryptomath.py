# Author: Bojan G. Kalicanin
# Date: 18-Mar-2017
# Description: Finding GCD - greatest common divisor using Euclid's Algorithm,
# and finding modular inverse using Euclid's Extended Algorithm.

def gcd(a, b):
    """Find greatest common divisor using Euclid's Algorithm"""
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    """Finding modular inverse using Euclid's Extended Algorithm"""
    # Returns modular inverse of a % m, which is the number i such that
    # (a* i) % m == 1

    if gcd (a, m) != 1:
        return None     # if a and m are not relatively prime numbers
                        # there is no mod inverse.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), \
            v1, v2, v3
    return u1 % m