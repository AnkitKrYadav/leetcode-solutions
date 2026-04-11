class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:
            if i == val :
                nums.remove(val)
        return len(nums)
#O(n^2) can be better by replacing rather removing