# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)  # A dummy node to form the new list
        current = dummy_head  # This will build the result linked list
        carry = 0  # Carry to keep track of sum > 10

        while l1 is not None or l2 is not None or carry != 0:
            # Get the values from l1 and l2, if they are not None
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Add the new value to the result linked list
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next nodes in l1 and l2
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # Return the resulting linked list, skipping the dummy node
        return dummy_head.next

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a set to store unique characters
        char_set = set()
        # Initialize pointers and the result variable
        left = 0
        max_length = 0

        # Iterate through the string
        for right in range(len(s)):
            # If the character at the right pointer is already in the set,
            # move the left pointer to remove the duplicate character
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the character to the set and update the maximum length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Even-length palindrome
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
 
# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if numRows is 1, return the original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the input string and populate the rows
        for char in s:
            rows[current_row] += char
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Join all the rows to form the final string
        return ''.join(rows)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Get the sign of x and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits by converting to string, reversing, and converting back to integer
        reversed_x = int(str(x)[::-1])
        
        # Restore the sign
        reversed_x *= sign
        
        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.

# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:
# Reading stops at the first non-digit character 'w'.


# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Ignore leading whitespaces
        s = s.strip()
        if not s:
            return 0
        
        # Step 2: Handle sign
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        # Step 3: Convert characters to integer until a non-digit is found
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
        
        # Apply the sign
        result *= sign
        
        # Step 4: Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer with the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        result = []
        
        # Step 2: Iterate through each element as the first element of the triplet
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first element
                continue
            
            # Step 3: Initialize two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum
        
        return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Integer to Roman

# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.

# Example 1:

# Input: num = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:

# Input: num = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII
# Example 3:

# Input: num = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
 
# Constraints:

# 1 <= num <= 3999

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Mapping of values to Roman symbols
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        roman_numeral = ""  # Result string for Roman numeral
        
        # Loop through the value-symbol pairs
        for value, symbol in value_symbols:
            # Append the symbol for each complete value in num
            while num >= value:
                roman_numeral += symbol
                num -= value
        
        return roman_numeral

# Example usage
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
