#Need to do this again (this is brute forced)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])

#NON BRUTE FORCE WAY

class Solution(object):
    def twoSum(self, nums, target):
        comp = {}
        for i in range(len(nums)):
            #how can I tie my current number with the target?
            #WAIT get target - number?
            if nums[i] in comp:
                return([i, comp[nums[i]]])
            comp[target - nums[i]] = i