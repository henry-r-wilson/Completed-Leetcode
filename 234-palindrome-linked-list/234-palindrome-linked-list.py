# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        num = []
        
        
        while head:
            num.append(head.val)
            head = head.next
        
        first = 0
        last = len(num) - 1
        
        while first <= last:
            if num[first] != num[last]:
                return False
            first += 1
            last -= 1
        return True
            
        
#This code turns the linked list into an array, and then deals with the array accordingly. First, we create an empty array, and then set a pointer at the beginning going forwards and a pointer at the end going backwards. It then goes a while loop, and says that while the pointer going backwards is further along than the pointer going frowards, keep going. Once this action is over, check to see if the value of the numbers from the pointer going forward equate to the value of the numbers from the pointer going backwards, and if so, claim true. 

#num = [] - Creates an empty array
        
#while head: - This states that while a linked list 'head' exists, do action

#num.append(head.val) - Action appends the value of the numbers from the linked list head into the blank array num
            
#head = head.next - Action makes sure the array moves forward one step each iteration

#first = 0 - The first pointer begins at the first node

#last = len(num) - 1 - The last pointer begins at the end, and goes backwards
        
#while first <= last: - This states that while the node value of the first pointer is less than the node value of the last point, keep going.

#if num[first] != num[last]: - If loop that states that if the num value for first doesn't equal the num value for last, do action

#return False - Action is to return question as false

#first += 1 - Move first node value along by 1
            
#last -= 1 - Move last node value backwards by 1
        
#return True - If False statement not triggered, return True


        
        
        
        
        

        