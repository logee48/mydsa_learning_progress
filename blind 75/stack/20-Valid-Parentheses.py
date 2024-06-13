# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


# my sol
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if no stack:
                stack.append(i)
            elif stack[-1]=="(" and i==")":
                stack.pop()
            elif stack[-1]=="{" and i=="}":
                stack.pop()
            elif stack[-1]=="[" and i=="]":
                stack.pop()
            else:
                stack.append(i)
        return stack==[]

# op sol:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack and stack[-1]=="(" and i==")":
                stack.pop()
            elif stack and stack[-1]=="{" and i=="}":
                stack.pop()
            elif stack and stack[-1]=="[" and i=="]":
                stack.pop()
            else:
                stack.append(i)
        return stack==[]