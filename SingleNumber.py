# Simply iterating through the array, hold a key value pair for the number and the amount of times it repeats

class Solution(object):
    def singleNumber(self, nums):
        dictionaryForNums = {}
        for i in nums:
            if i in dictionaryForNums:
                dictionaryForNums[i] += 1
            else:
                dictionaryForNums[i] = 1
        
        for key in dictionaryForNums:
            if (dictionaryForNums[key] != 2):
                return key


# IS this the right solutoin? It requires you to havea linear runtime complexity and use constant space.

# Well, it definitely is linear runtime, but in terms of extra space, it isnt. For this, we need to use the XOR operator in python (^)

class Solution(object):
    def singleNumber(self, nums):
        singleNum = 0
        for i in nums:
            singleNum = singleNum ^ i # ^ is the XOR bitwise operator
        return singleNum