from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(i, nums[nums[i]])
        print(ans)


# Solution().buildArray([0, 2, 1, 5, 3, 4])
Solution().buildArray([5, 0, 1, 2, 3, 4])
