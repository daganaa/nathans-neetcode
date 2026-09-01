class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ret = 0

        for num in numSet:
            if num-1 not in numSet:
                l = 1
                while num+1 in numSet:
                    num += 1
                    l += 1
                ret = max(ret, l)
        return ret