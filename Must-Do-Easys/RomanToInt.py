class Solution:
    def romanToInt(self, s: str) -> int:
        # LVIII
        # first element L, 
        conversionDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        i = 0
        while i < len(s):
            if i+1 != len(s):      
                if conversionDict[s[i]] >= conversionDict[s[i+1]]:
                    num += conversionDict[s[i]]
                    i += 1
                else:
                    num += conversionDict[s[i+1]] - conversionDict[s[i]]
                    i += 2
            else:
                num += conversionDict[s[i]]
                i += 1
        return num
                