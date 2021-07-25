# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    # keep track of two pointers symbolizing positions in the current valid
    # paranthesis sequence. when they are equal, add their combined values
    # and compare to see if the sequence is longer than the current longest
    # sequence. has to be done forward and backward because of sequences ending
    # at the end of the string.
    def longestValidParentheses(self, s: str) -> int:
        left = right = longest = 0

        # forward loop
        for i in range(len(s)):
            # increment left on finding a (, and ) otherwise
            if s[i] == '(':
                left += 1
            else:
                right += 1

            # if they're equal, add their combined value and check to see if
            # it's longer than the current longest sequence.
            if left == right:
                longest = max(longest, left + right)

            # if right is larger than left, the sequence has an extra ),
            # making it impossible to be valid.
            elif right >= left:
                left = right = 0
        left = right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1

            if left == right:
                longest = max(longest, left + right)
            elif left >= right:
                right = left = 0

        return longest
