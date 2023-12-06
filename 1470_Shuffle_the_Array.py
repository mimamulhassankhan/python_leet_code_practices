from typing import List


class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    #     left, right = nums[:n], nums[n:]
    #     result = list()
    #     for i in range(n):
    #         result.extend([left[i], right[i]])
    #     return result

    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    #     ans=[]
    #     for i in range(len(nums)//2):
    #         for j in range(i,len(nums),n):
    #             ans.append(nums[j])
    #     return ans

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half, second_half = nums[:n], nums[n:]
        return [x for pair in zip(first_half, second_half) for x in pair]


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(Solution().shuffle([1, 1, 2, 2], 2))
