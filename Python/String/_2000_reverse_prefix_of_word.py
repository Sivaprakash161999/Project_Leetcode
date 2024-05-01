

class Solution:
    # string - O(n) time; O(1) space
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = None
        for i, c in enumerate(word):
            if c == ch:
                ch_idx = i
                break
        if not ch_idx:
            return word
        return word[ch_idx::-1] + word[ch_idx + 1:]

    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[i::-1] + word[i+1:]
        return word

    # two-pointers
    def reversePrefix(self, word: str, ch: str) -> str:
        res = list(word)
        left = 0
        for right in range(len(word)):
            if res[right] == ch:
                while left <= right:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
                return "".join(res)
        return word

    # stack
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = []
        index = 0
        while index < len(word):
            stack.append(word[index])
            if word[index] == ch:
                while stack:
                    result.append(stack.pop())
                index += 1
                while index < len(word):
                    result.append(word[index])
                    index += 1
                return ''.join(result)
            index += 1
        return word



        