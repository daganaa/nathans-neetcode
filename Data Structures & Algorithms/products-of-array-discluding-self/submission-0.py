class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            pre = 1 
            post = 1
            for j in range(i):
                pre *= nums[j]
            for j in range(i+1, len(nums)):
                post *= nums[j]
            ret.append(pre*post)
        return ret