class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left_list = self.sortList(head)
        right_list = self.sortList(mid)

        return self.merge(left_list, right_list)

    def merge(self, left_list: ListNode, right_list: ListNode) -> ListNode:
        merged_head = ListNode()
        merged_tail = merged_head

        while left_list and right_list:
            if left_list.val < right_list.val:
                merged_tail.next = left_list
                left_list = left_list.next
            else:
                merged_tail.next = right_list
                right_list = right_list.next

            merged_tail = merged_tail.next

        merged_tail.next = left_list if left_list else right_list
        return merged_head.next


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next=ListNode(-1)

    solution = Solution()
    sorted_head = solution.sortList(head)

    while sorted_head:
        print(sorted_head.val, end=" -> ")
        sorted_head = sorted_head.next
