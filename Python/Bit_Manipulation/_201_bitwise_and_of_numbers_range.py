

class Solution:
    # Bit-manipulation - Time = (logn(left) + logn(right)), space = O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''We need to find the common prefix of
            left and right in their binary representation'''
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        # if left == right means, there is a common prefix
        # we now shift that prefix back to its original place
        # by the count of bits we removed.
        return left << count

    # Brian Kernighan's Algo: Time = O(1), Space = O(1)
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''right & (right - 1) unsets the right most set bit 
            of right; by doing so we reduce the right bit wise
            and check if it is equal to left (common prefix)
            and return if it is'''
        if left == 0:
            return 0
        while right > left:
            right &= (right - 1)
        return right