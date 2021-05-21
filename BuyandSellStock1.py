import sys

class Solution(object):
    def maxProfit(self, prices):
        maxProf = 0
        minPrice = sys.maxint
        for i in range(0, len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            elif (prices[i] - minPrice > maxProf):
                maxProf = prices[i] - minPrice
        
        return maxProf
                
            #solution behind this is, whenever a new minprice is found, it will compare with the current number
            #if it gives the greatest possible difference (maxProf)