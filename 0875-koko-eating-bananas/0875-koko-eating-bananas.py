class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fintime(speed):
            time = 0
            for i in piles:
                time += math.ceil(i/speed) 
            return time

        low,high=1,max(piles)
        while low < high:
            mid = (low+high)//2
            if fintime(mid) > h:
                low = mid+1
            else:
                high = mid
        return high
      

#O(nlogM)