from typing import List


class Solution:
    # def subListOfTwoElements(self, lst: List[int], index=0):
    #     if index >= len(lst):
    #         return []
    #     else:
    #         subsets = self.subListOfTwoElements(lst, index + 1)
    #         new_subsets = [[lst[index], lst[i]] for i in range(index + 1, len(lst))]
    #         return new_subsets + subsets

    def subsets_of_two(self, lst, index=0):
        if index >= len(lst):
            return set()
        else:
            subsets = self.subsets_of_two(lst, index + 1)
            new_subsets = {
                tuple(sorted([lst[index], lst[i]])) for i in range(index + 1, len(lst))
            }
            return new_subsets.union(subsets)

    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        subsets = self.subsets_of_two(nums)
        print("__subsets__", subsets)
        for subset in subsets:
            if subset[0] == subset[1]:
                good_pairs += 1
        return good_pairs


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(Solution().numIdenticalPairs([1, 1, 1, 1]))
print(Solution().numIdenticalPairs([1, 2, 3]))
print(Solution().numIdenticalPairs([]))
