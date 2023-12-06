from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums) - 1):
            for num_dd in range(num + 1, len(nums)):
                if nums[num] + nums[num_dd] == target:
                    return [num, num_dd]


solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)
