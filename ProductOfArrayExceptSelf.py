# Runtime: 308 ms, faster than 25.88% of Python online submissions for Product of Array Except Self.
# Memory Usage: 20 MB, less than 89.69% of Python online submissions for Product of Array Except Self.
class Solution(object):
    def productExceptSelf(self, nums):
        dictHoldingAllValues = {}
        for i in range(len(nums)):
            if nums[i] in dictHoldingAllValues:
                dictHoldingAllValues[nums[i]] += 1
            else:
                dictHoldingAllValues[nums[i]] = 1
        
        #{ 1:1, 2:1, 3:1, 4:1 }
        print(dictHoldingAllValues)
        
        for i in range(len(nums)):
            product = 1
            for key,value in dictHoldingAllValues.items():
                if nums[i] == key:
                    if value > 1:
                        product *= key**(value-1)
                    pass
                else:
                    product *= key**value
            nums[i] = product

        return nums

# TRY 2 - Better runtime + O(1) memory usage

class Solution(object):
    def productExceptSelf(self, nums):
        resultingArray = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            resultingArray[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            resultingArray[i] *= postfix
            postfix *= nums[i]
        return resultingArray
                

# Review this one