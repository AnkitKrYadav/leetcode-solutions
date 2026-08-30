class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        di={nums[0]:1}
        ns=set()
        c=0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                di[nums[i]] = di.get(nums[i],0)+1
        print(di)
        for i in di.values():
            if i==1:
                c+=1
        return c
            