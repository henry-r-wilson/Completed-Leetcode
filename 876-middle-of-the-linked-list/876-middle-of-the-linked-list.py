# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
            
#This code utilises pointers. A fast pointer and a slow pointer start at the beginning of the linked list, with the fast pointer moving one step forward and the slow moving two steps forward. We can say that once the fast pointer reaches the end, the slow pointer will be at the halfway point. Therefore, we say that while there exists a node after the current node the fast pointer is on, keep moving forward. Once there isn't, stop the pointer and return the values from the slower pointer at the mid-point onwards. This provides our result.

#slow, fast = head, head - This states that the beginning of the linked list, head, has two pointers on it called slow and fast.

#while fast and fast.next: - This states that while there is both a fast and a fast.next that exists, do action. This is done to make sure fast stops at the last point, while fast.next stops outside the range. 

#fast = fast.next.next - This states that fast pointer should move two nodes at a time

#slow = slow.next - This states that slow pointer should move one node at a time 

#return slow - Once the while loop is False, return the value of slow. Since this is a linked list, the return will give all values including and after where the slow point stops.

        