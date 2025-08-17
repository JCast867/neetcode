'''
PROBLEM DESCRIPTION

Contains Duplicate
Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''
class Solution:
    '''
    EXPLANATION

    What I do is create an empty hashmap
    Iterate through the list `nums`
    If the element is not in the hashmap,
    then I add that element in to and itialize a value of 1
    If it is in the hashmap,
    then I return True since it's a duplicate and it exists already

    If nothing returns from the previous for loop,
    then I return False since it has no duplicates

    The time complexity will be O(n) with space complexity being O(n)
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Taking in a list of integers and return a boolean
        '''
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return True
        return False