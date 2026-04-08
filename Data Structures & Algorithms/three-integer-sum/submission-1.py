class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i-1] == a:
                continue

            l, r = i+1, (len(nums)-1)
            while l < r:
                if nums[l]+nums[r] == -a:
                    ret.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l]+nums[r] < -a:
                    l += 1
                else:
                    r -= 1
        return ret