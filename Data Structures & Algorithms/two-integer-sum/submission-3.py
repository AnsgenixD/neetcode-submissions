class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # Starts after i so we don't reuse elements
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
                
        