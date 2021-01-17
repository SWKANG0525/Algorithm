"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""
import re


def is_palindrome(self, words: str) -> str:
    words = words.lower()  # Preprocessing words
    words = re.sub('[^a-z0-9]', '', words)  # Filtering Other Characters by RegEx

    return words == words[::-1]  # String Slicing
