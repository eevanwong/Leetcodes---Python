class Solution(object):
    def construct2DArray(self, original, m, n):
        if (len(original) != m*n):
            return []
        else:
            arrayToReturn = []
            for i in range(m):
                innerArray = []
                #[ m rows where each row will have n columns ]
                for j in range(n):
                    innerArray.append(original[i*n+j])
                arrayToReturn.append(innerArray)
            return arrayToReturn


#O(m*n) runtime 

#Not the best, we can do better, the next soluition I have is with splicing, which is a bit better as we dont need the inner loop

class Solution(object):
    def construct2DArray(self, original, m, n):
        if (len(original) != m*n):
            return []
        else:
            arrayToReturn = []
            for i in range(m):
                arrayToReturn.append(original[i*n:i*n+n])
            return arrayToReturn

# leverage splicing