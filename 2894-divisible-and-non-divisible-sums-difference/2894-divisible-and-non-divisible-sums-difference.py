class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        for i in range (1,n+1):
            num1 += -i if i%m == 0 else + i
        return num1