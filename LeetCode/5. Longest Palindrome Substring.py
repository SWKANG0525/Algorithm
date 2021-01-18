"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        # Palindrome discriminant & Two-pointer expand
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        # Exception Condition
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""

        for idx in range(len(s)):
            result: str = max(result, expand(idx, idx + 1), expand(idx, idx + 2), key=len)

        return result
