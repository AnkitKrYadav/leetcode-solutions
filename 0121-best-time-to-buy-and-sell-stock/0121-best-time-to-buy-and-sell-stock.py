class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp,i,j=0,0,1
        while j < len(prices):
            if prices[j] < prices[i]:
                i=j
            else:
                mp=max(prices[j] - prices[i],mp)
            j+=1
        return mp
