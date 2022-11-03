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


  
# 13 Roman to integer   08/09/2022
# mistake i did, didn't read the question properly
# MCMXCIV in 2nd iteration CM will be compared and C<M is true, so we need to add M-C to sum and skip M in next part and go to XC


class Solution:
    def romanToInt(self, s: str) -> int:
        sum_val = 0
        r_val = {'I':1, 'V':5, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};      #using dist to store roman values
        length = 0                 #using while because after compare statement passed we need to ""skip one iteration part""
        if(len(s)>1):
            while(length<len(s)-1):
                if(r_val[s[length]] < r_val[s[length+1]]):
                    sum_val += r_val[s[length+1]] - r_val[s[length]]
                    length+=2
                else:
                    sum_val += r_val[s[length]]
                    length+=1
            if(r_val[s[-2]] >= r_val[s[-1]]):               #if last ele is less than 2nd to last, add last ele to sum_val
                sum_val+=r_val[s[-1]]
        else:                                     #for single char test case
            sum_val+= r_val[s]

        return sum_val
    
    
# 844 Backspace string compare   08/09/2022
# i didn't solve it on my own, i saw solution is diss part
# using stack this problem can be solved
# understood where to use stack
"""testcase
s = "ac#d"
t = "ace##d"
if u get #, then remove element before #
s = ad
t = ad
output: true, hence s==t
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        one = []
        two = []
        for i in range(len(s)):
            if (s[i] != "#"):
                one.append(s[i])
            else:
                if(one!=[]):
                    one.pop(-1)
        for i in range(len(t)):
            if (t[i]!= "#"):
                two.append(t[i])
            else:
                if(two!=[]):
                    two.pop(-1)
        return one==two
    
    
    
# 20 valid parentheses
# read the questions properly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""  test case 
(()) flase
(){}[] true
([) flase
))(( flase """

# ik not a optimal sol, but i tried on my own =)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = 1
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif(len(stack)!=0):
                if (i==")" and stack[-1]=="(") or (i=="]" and stack[-1]=="[") or (i=="}" and stack[-1]=="{"):
                    stack.pop()
                else:
                    flag = 0
            else:
                flag = 0
        if(len(stack)==0 and flag==1):
            return True
        else:
            return False
        
        
        
# 953. Verifying an Alien Dictionary
# solved with help of solution


def alien(a,word):
    hashmap = {}
    for i in range(len(a)):
        hashmap.update({a[i]:i})
        #hashmap[a[i]] = i
    for i in range(len(word)-1):
        for j in range(len(word[i])):
            #print(i,j)
            if j >= len(word[i+1]):
                return False
            if word[i][j] != word[i+1][j]:
                # print(hashmap[word[i][j]], hashmap[word[i+1][j]])
                if(hashmap[word[i][j]] > hashmap[word[i+1][j]]):
                    return False
                else:
                    break;
    return True

a = "hlabcdefgijkmnopqrstuvwxyz"
word = ["hello","leetcode"]
print(alien(a,word))




# valid Anagram

def anagram(s,t):
    ss = {}
    tt = {}
    for i in s:
        ss[i] = s.count(i)
    for i in t:
        tt[i] = t.count(i)
    return ss == tt


# 70 climbing stairs
# it is trickyy question, u can only climb 1 or 2 step at a time
# nothing special just fibanociii
"""
test case: 
n = 2
1,1
2
answer = 2

n = 1
1
answer = 1

n = 3
1,1,1
2,1
1,2
answer = 3

n = 4
1,1,1,1
2,1,1
1,2,1
1,1,2
2,2
answer = 5
"""
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:return 1
        else:
            a = 1
            b = 2
            for i in range(n-2):
                c = a
                a = b
                b = c+b
            return b


