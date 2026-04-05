class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans = [0]*len(temperatures)
        day = 0
        while day < len(temperatures):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                ans[stack[-1]] = day - stack[-1]
                stack.pop()
            stack.append(day)
            day += 1
        return ans
