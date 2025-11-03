class Solution(object):
        
    def isPalindrome(self, x):    # No extra indentation before def
        if x < 0:                # Proper indentation (4 spaces)
            return False
        return str(x) == str(x)[::-1]
