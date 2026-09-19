class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return not (1<<30)%n