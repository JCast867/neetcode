'''
PROBLEM DESCRIPTION

Valid Anagram
Easy

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
'''
class Solution:
    '''
    EXPLANATION

    What I do is initialize 2 hashmaps
    1 for each string
    I iterate through the first parameter
    If that letter doesn't exists in the hashmap,
    then I add it with a value of 1
    If it is in the hashmap,
    then I add 1 to the value

    I do the exact same thing for the second parameter

    Then I check if the hashmaps are the same
    If they're the same,
    then I return True
    If not,
    then I return False

    The time complexity will be O(n+m) with a space complexity of O(n+m)
    Space complexity is not optimal but it makes the code much more readable
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Takes in two parameters strings, `s` and `t`
        and we're supposed to return a boolean
        '''
        dic1 = {}
        dic2 = {}
        for letter in s:
            if letter not in dic1:
                dic1[letter] = 1
            else:
                dic1[letter] += 1
            
        for letter in t:
            if letter not in dic2:
                dic2[letter] = 1
            else:
                dic2[letter] += 1

        if dic1 == dic2:
            return True
        return False