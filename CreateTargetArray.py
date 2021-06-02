class Solution(object):
    def createTargetArray(self, nums, index):
        #assuming that the length of the nums and index are equivalent
        tarArr = []
        i = 0
        while i < len(nums):
            tarArr.insert(index[i],nums[i])
            i+=1
        return tarArr