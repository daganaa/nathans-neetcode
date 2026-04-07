class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = dict()
        for idx, num in enumerate(nums):
            A[num] = idx
        for i in range(len(nums)):
            if target - nums[i] in A and i != A[target - nums[i]]:
                return [i, A[target - nums[i]]]