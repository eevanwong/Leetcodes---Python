# brute force solution, O(n) runtime BUT not constant extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        a = []
        for i in range(len(nums)):
            if nums[i] in s:
                a.append(nums[i])
            else:
                s.add(nums[i])
        return a


# NOTE: Constant extra space refers to any other space that doesn't involve what you're returning (i.e, if you're using a new array to return, that doesnt countas extra space) 
# new solution, with constant extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                a.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] *= -1
        return a

#in this solution, The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative

#we can go in depth in this solution with this: https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

