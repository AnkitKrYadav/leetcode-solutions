class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prepro=[1 for _ in range(len(nums))]
        sufpro=[1 for _ in range(len(nums))]
        i,j = 1,-2
        while i < len(nums) and j >= -len(nums):
            prepro[i]=prepro[i-1]*nums[i-1]
            sufpro[j]=sufpro[j+1]*nums[j+1]
            i+=1;j-=1

        return [ sufpro[i]*prepro[i] for i in range(len(nums)) ]
