class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetTime = 0
        fleetCount = 0
        sp = sorted(zip(position,speed),reverse=True)

        for p,s in sp:
            currentTime = (target - p)/s 
            if currentTime > fleetTime:
                fleetCount += 1
                fleetTime = currentTime

        return fleetCount

#O(nlogn), O(1)