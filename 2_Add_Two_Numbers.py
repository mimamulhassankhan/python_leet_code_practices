# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convertSingleLinkedListToDecimalNumber(self, l: Optional[ListNode]) -> int:
        l_num = 0
        l_num_str = ""
        while l:
            l_num_str += str(l.val)
            l = l.next
        l_num = int(l_num_str[::-1])
        return l_num

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_num = self.convertSingleLinkedListToDecimalNumber(l1)
        l2_num = self.convertSingleLinkedListToDecimalNumber(l2)
        l_sum = str(l1_num + l2_num)[::-1]
        l_sum_head = ListNode(l_sum[0])
        l_sum_tail = l_sum_head
        for i in range(1, len(l_sum)):
            l_sum_tail.next = ListNode(l_sum[i])
            l_sum_tail = l_sum_tail.next
        return l_sum_head


solution = Solution()

# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
resultInSinglyList = solution.addTwoNumbers(
    ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    ),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
)

# print resultInSinglyList
while resultInSinglyList:
    print(resultInSinglyList.val)
    resultInSinglyList = resultInSinglyList.next
