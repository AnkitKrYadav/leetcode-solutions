class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans = [0]*len(temperatures)

        for day in range(len(temperatures)):

            while stack and temperatures[day] > temperatures[stack[-1]]:
                ans[stack[-1]] = day - stack[-1]
                stack.pop()

            stack.append(day)
        return ans
