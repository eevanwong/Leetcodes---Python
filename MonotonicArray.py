#brute force
#nah nvm its not brute force, this is O(n) it's the same as the rest of the solutions
class Solution(object):
    def isMonotonic(self, A):
        isIncreasing = True
        isDecreasing = True
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                isDecreasing = False
            elif A[i] > A[i+1]:
                isIncreasing = False
        return(isIncreasing or isDecreasing)