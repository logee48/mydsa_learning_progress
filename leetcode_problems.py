#2 add two numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode()
      current = dummy
      carry = 0   #if we have nodes with 5+9 answer supples to be 1->4 not a node with 14
      while l1 or l2 or carry:   # what if we have 0,0 but carry is has val
        val1 = l1.val if l1 else 0  #store l1 value to val1 is l1 is none store 0
        val2 = l2.val if l2 else 0  
        sum_val = val1+val2+carry   # basic math 
        carry = sum_val // 10       # getting carry by using float div 73//10 answer=7
        sum_val = sum_val % 10      # after getting carry remove font val 73%10 answer=3
        carry = carry.next               #next three steps making next connection to next node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
      return dummy.next             # dummy first val is None, so values are stored from next to head node
    
