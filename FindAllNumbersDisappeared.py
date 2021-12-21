class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        if (n > 1):
            dictionaryForDealingWithDuplicates = {}
            newArr = []
            for i in nums:
                if i in dictionaryForDealingWithDuplicates:
                    pass
                else:
                    dictionaryForDealingWithDuplicates[i] = 0
            
            for i in range(1, n + 1):
                if i not in dictionaryForDealingWithDuplicates:
                    newArr.append(i)
            return newArr
        else:
            return [1]

#Now, if you want to deal with duplicates and not have to worry about the value of the key value pair dont use dictionarys just use sets.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        if (n > 1):
            setForDuplicates = set()
            newArr = []
            for i in nums:
                if i in setForDuplicates:
                    pass
                else:
                    setForDuplicates.add(i)
            
            for i in range(1, n + 1):
                if i not in setForDuplicates:
                    newArr.append(i)
            return newArr
        else:
            return [1]

# And when you want a really pythonic solution:

class Solution(object):
    def findDisappearedNumbers(self, nums):
        return list(set(range(1,len(nums)+1)) - set(nums))
    
# in terms of performance tho, they all have similar numbers