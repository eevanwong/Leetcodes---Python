# Runtime: 12 ms, faster than 98.51% of Python online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 13.6 MB, less than 19.01% of Python online submissions for Check If Two String Arrays are Equivalent.

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return(''.join(word1) == ''.join(word2))
        