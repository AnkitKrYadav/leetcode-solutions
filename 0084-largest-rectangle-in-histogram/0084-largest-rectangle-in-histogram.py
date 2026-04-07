class Solution:
    def largestRectangleArea(self, hts: List[int]) -> int:
        marea=0
        lstack= [-1]*len(hts)
        rstack= [len(hts)]*len(hts)
        stack= []
        #left smaller
        for i in range(len(hts)):
            while stack and hts[stack[-1]] >= hts[i]:
                stack.pop()
            if stack:
                lstack[i] = stack[-1]
            stack.append(i)
        stack.clear()
        
        #right smaller
        for i in range(len(hts)-1,-1,-1):
            while stack and hts[stack[-1]] >= hts[i]:
                stack.pop()
            if stack:
                rstack[i] = stack[-1]
            stack.append(i)
        
        #computing each area and taking max
        for i in range (len(hts)):
            width = rstack[i] - lstack[i] -1
            marea = max(width * hts[i],marea)
        return marea