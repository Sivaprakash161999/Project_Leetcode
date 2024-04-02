

class Solution:
    # hashmap and hashset - O(n) time; O(n) space
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''Each unique character in S
            should be mapped to a unique 
            character in T and vice-versa.
            No character in T should be mapped
            to multiple characters in S.'''
        
        # char_map maps the character of s to t
        char_map = {}
        # alloted keeps tracks of the characters in t
        # which are already mapped to other characters in s
        alloted = set()
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] not in alloted:
                    char_map[s[i]] = t[i]
                    alloted.add(t[i])
                else:
                    return False
            if char_map[s[i]] != t[i]:
                return False
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t)))  ==  len(set(s))  ==  len(set(t))
        