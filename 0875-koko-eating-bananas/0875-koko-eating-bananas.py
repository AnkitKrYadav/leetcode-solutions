class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low < high:
            mid = (low+high)//2
            if self.fintime(mid,piles) > h:
                low = mid+1
            else:
                high = mid
        return high
            
    
    def fintime(self,speed,piles):
        time = 0
        for i in piles:
            time += math.ceil(i/speed) 
        return time

#O(nlogn)