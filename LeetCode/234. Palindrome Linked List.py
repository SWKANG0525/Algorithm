"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse_linked_list = None
        fast_pointer = slow_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            reverse_linked_list, reverse_linked_list.next, slow_pointer = slow_pointer, reverse_linked_list, slow_pointer.next

        if fast_pointer:
            slow_pointer = slow_pointer.next

        while reverse_linked_list and reverse_linked_list.val == slow_pointer.val:
            slow_pointer = slow_pointer.next
            reverse_linked_list = reverse_linked_list.next

        return not reverse_linked_list
