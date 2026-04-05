class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finishTime = [float('inf')] * len(position)
        fleetLead = len(finishTime) -1
        fleetCount = 1
        sp = sorted(zip(position,speed))

        for i in range (len(sp)):
            p,s = sp[i]
            finishTime[i] = (target - p)/s

        for car in range (len(finishTime)-2,-1,-1):
            if finishTime[car] > finishTime[fleetLead]:
                fleetCount += 1
                fleetLead = car

        return fleetCount

#nlogn can be better by combing both for loop into and direct cal without storing and fetching again
