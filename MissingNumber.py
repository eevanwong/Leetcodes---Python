# Solution 1, figured out to get the sum of all of them then compare it with the sum of the other one, came up with this

class Solution(object):
    def missingNumber(self, nums):
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            return 1
        
        highestVal = 0
        currentSum = 0
        
        for i in range(len(nums)):
            if nums[i] > highestVal:
                highestVal = nums[i]
            currentSum += nums[i]
                
        expectedSum = 0
        for i in range(0, highestVal+1):
            expectedSum += i
        
        if currentSum == expectedSum:
            if 0 in nums:
                return highestVal+1
            return(0)
        
        else:
            return(expectedSum-currentSum)
        
# Solution 2 - much shorter, pythonic solution, involves the equation for getting the sum of all counting numbers
#(n / 2)(first number + last number) = sum
# therefore, get this for the expected sum, then get the actual sum from iterating through an array or using the sum() method in python

class Solution(object):
    def missingNumber(self, nums):
        numberOfNums = len(nums)
        expectedSum = (numberOfNums*(numberOfNums+1)/2)
        actualSum = 0
        
        for i in nums:
            actualSum += i
        
        return expectedSum - actualSum
    

#regardless there didn't seem to be much of a performance difference, both solutions seemed to have worked a bit