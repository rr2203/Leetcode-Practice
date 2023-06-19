# TC: O(log2(dividend)) SC: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and dividend == -2147483648: return 2147483647  # Integer.MAX_VALUE
        isPositive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            num_shift = 0

            while dividend >= (divisor << num_shift):
                num_shift += 1

            num_shift -= 1

            result += 1 << num_shift
            dividend -= (divisor << num_shift)

        return result if isPositive else -result