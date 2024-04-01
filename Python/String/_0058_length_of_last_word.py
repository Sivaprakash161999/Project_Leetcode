


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # the strip method removes the leading
        # trailing whitespaces in a string;
        # the split method, splits the given string
        # into a list of words, using the given delimiter
        # default delimiter is ' '
        return len(s.strip().split()[-1])

    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        # traverse the string in reverse
        for i in range(len(s) - 1, -1, -1):
            # if there are already some characters
            # found, and the current character is 
            # whitespace, return the count
            if s[i] == ' ' and count:
                return count
            elif s[i] != ' ':
                count += 1
        return count

        