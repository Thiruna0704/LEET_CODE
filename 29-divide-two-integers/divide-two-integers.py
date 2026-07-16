class Solution(object):
    def divide(self, dividend, divisor):

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            dividend -= temp
            ans += multiple

        return sign * ans