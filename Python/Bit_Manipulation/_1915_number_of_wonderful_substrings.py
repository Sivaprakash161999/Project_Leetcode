from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # create the frequency map
        # key = bitmask, value = frequency of bitmask key
        freq = {}

        # the empty prefix can be the smaller prefix, 
        # which is handled like this
        freq[0] = 1

        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - ord('a')

            # Flip the parity of the c-th bit in the runnning prefix mask
            mask ^= (1 << bit)

            # Count smaller prefixes that create substring with no 
            # odd occuring letters
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            
            # Loop through every possible letter that can appear
            # an odd number of times in a substring
            for odd_c in range(0, 10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]
        
        return res


    # hash table + prefix sum - O(n) time; O(n) space
    def wonderfulSubstrings(self, word: str) -> int:
        # to keep track of previously occured prefix masks
        # and their frequencies
        # key: prefix_mask, value: frequency
        prefix_masks = {}
        # to represent an empty string
        # it's prefix mask is 0
        prefix_masks[0] = 1
    
        res = 0
        mask = 0 # mask of current prefix of word
                 # each bit will represent the parity of 
                 # letters - 'a' 0th bit and 'j' 9th bit
                 # if the bit is set, the letter appears odd times
                 # otherwise, the letter appears even times
        for c in word:
            idx = ord(c) - ord('a')
            mask ^= (1 << idx)

            # if the mask already present in prefix_masks,
            # then all the substrings between these 2 prefixes
            # has even number of all letters,
            # i.e) no letter is present odd number of times
            if mask in prefix_masks:
                res += prefix_masks[mask]
                prefix_masks[mask] += 1
            else:
                prefix_masks[mask] = 1

            # now, for the substrings that contains
            # only one letter odd times,
            # such, substring will differ from our
            # current prefix mask by at most 1 bit
            # so, for each different letter 'a' to 'j'
            # we will revert the bit at respective index 
            # and check if such prefix is already present
            # and add it to result
            for idx in range(10):
                if (mask ^ (1 << idx)) in prefix_masks:
                    res += prefix_masks[mask ^ (1 << idx)]
        
        return res

    def wonderfulSubstrings(self, word: str) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        res = 0
        mask = 0
        for c in word:
            mask ^= (1 << (ord(c) - ord('a')))
            res += prefix[mask]
            for i in range(10):
                res += prefix[mask ^ (1 << i)]
            prefix[mask] += 1
        return res


    def wonderfulSubstrings(self, word: str) -> int:
        to_bit = {c: (1 << i) for i, c in enumerate(ascii_lowercase[:10])}
        mask = 0
        count = defaultdict(int)
        count[0] += 1
        for c in word:
            mask ^= to_bit[c]
            count[mask] += 1
        res = 0
        for mask, cnt in count.items():
            res += cnt * (cnt - 1) // 2
            for i in range(10):
                mask2 = mask ^ (1 << i)
                if mask2 < mask:
                    res += cnt * count.get(mask2, 0)
        return res






