# Runtime: 1416 ms, faster than 5.11% of Python online submissions for Arranging Coins.
# Memory Usage: 13.3 MB, less than 88.35% of Python online submissions for Arranging Coins.

class Solution(object):
    def arrangeCoins(self, n):
        num = 1
        while n > 0:
            n -= num
            num += 1
            if n - num < 0:
                return(num-1)
            elif n - num == 0:
                return(num)
        if n <= 0:
            return(n)

