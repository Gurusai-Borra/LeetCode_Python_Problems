class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            
            res = res * 10 + digit

        res *= sign

        if res < INT_MIN or res > INT_MAX:
            return 0

        return res
