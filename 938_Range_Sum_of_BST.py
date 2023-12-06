# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root:
            if root.val >= low and root.val <= high:
                sum += root.val
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)
        return sum


solution = Solution()
# result = solution.rangeSumBST(
#     TreeNode(
#         10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
#     ),
#     7,
#     15,
# )

# root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
result = solution.rangeSumBST(
    TreeNode(
        10,
        TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
        TreeNode(15, TreeNode(13), TreeNode(18)),
    ),
    6,
    10,
)
print(result)
