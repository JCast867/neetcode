'''
PROBLEM DESCRIPTION

Valid Parentheses
Easy

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
'''

class Solution:
    '''
    EXPLANATION

    Initialize the stack
    Loop through each bracket in the string
    If the bracket is an opening bracket
    then we push it to the stack
    But if it's a closing bracket
    then we check to see if it matches with the one on top of the stack
    If it doesn't
    then we return False
    If it does match
    then we pop the opening bracket off the stack
    Additionally there's an edge case which is why we check if the length 
    of the stack is less than or equal to 0 when there's a closing bracket
    If the length is less than or equal to 0
    then we return False to avoid this string "]"

    At the end we check if the stack is empty
    If it is empty
    then we return True since each parentheses is satisfied with its partner
    If it's not
    then we return False
    '''
    def isValid(self, s: str) -> bool:
        # takes in a string and returns a boolean
        stack = []
        for brk in s:
            if brk == "(" or brk == "{" or brk == "[":
                stack.append(brk)
            elif brk == ")":
                if len(stack) <= 0:
                    return False
                last = stack[-1]
                if last != "(":
                    return False
                else:
                    stack.pop()
            elif brk == "}":
                if len(stack) <= 0:
                    return False
                last = stack[-1]
                if last != "{":
                    return False
                else:
                    stack.pop()
            elif brk == "]":
                if len(stack) <= 0:
                    return False
                last = stack[-1]
                if last != "[":
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        return False
    