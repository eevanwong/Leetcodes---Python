#now, you'd be surprised that this actually got decent results 
# Runtime: 20 ms, faster than 62.73% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.5 MB, less than 84.86% of Python online submissions for Valid Parentheses.

#i thought you needed to use recursion, nah it doesnt 
#runtime of this is o(n)

class Solution(object):
    def isValid(self, s):
        dictionary = {'(':')','[':']','{':'}' }
        openArr = []
        closArr = []
        if len(s) % 2 != 0: #if its odd, then no way it can be balanced
            return(False)
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                openArr.append(s[i])
                closArr.append(dictionary[s[i]])
            else:
                if len(openArr) == 0:
                    return(False)
                if s[i] == dictionary[openArr[len(openArr)-1]]:
                    closArr.pop()
                    openArr.pop()
                else:
                    return(False)
            if len(openArr) > len(s)-i:
                return(False)
        return(True)
            

#Recursive Solution
