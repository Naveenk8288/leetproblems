
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits manually
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            result = result * 10 + digit

            # Step 4: Handle 32-bit overflow
            if sign * result > INT_MAX:
                return INT_MAX

            if sign * result < INT_MIN:
                return INT_MIN

            i += 1

        # Step 5: Return final integer
        return sign * result

        