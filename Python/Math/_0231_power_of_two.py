from math import log2, trunc

pow_of_2 = set(2**i for i in range(31))

class Solution:

    # bit manipulation
    def isPowerOfTwo(self, n: int) -> bool:
        '''bitwise And of powers of 2 and (powers of 2 - 1)
            will be 0: 
            n & (n - 1) = 0
            negative numbers cannot be powers of 2'''
        return n > 0 and (n & (n - 1) == 0)

    # iterative
    def isPowerOfTwo(self, n: int) -> bool:
        '''Powers of 2 will only have 1 set bit'''
        if n > 0:
            ones = 0
            while n:
                ones += (n & 1)
                n >>= 1
            return ones == 1
        return False

    # iterative
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

    # Recursive
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))

    # log function
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log2(n) == trunc(log2(n))

    # Math
    def isPowerOfTwo(self, n: int) -> bool:
        '''only a power of 2 will divide a larger power of 2'''
        return n > 0 and (1 << 31) % n == 0

    # precomputing
    def isPowerOfTwo(self, n):
        return n in pow_of_2
        