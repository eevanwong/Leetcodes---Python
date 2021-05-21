# Runtime: 228 ms, faster than 76.29% of Python online submissions for Array Partition I.
# Memory Usage: 15.5 MB, less than 66.33% of Python online submissions for Array Partition I.

class Solution(object):
    
    def arrayPairSum(self, nums):
        maxOutput = 0

        #sort for equal order
        nums.sort()

        #It will compare index i, then index i*2 (which will always compare the smallest of pair)
        #e.g it will add 0 (which is min of first pair), then 2 (min of second pair), and so on (will alsoways add 2n index which is always min)
        for i in range(len(nums)/2):
            maxOutput += nums[i*2]
        return(maxOutput)