class Solution(object):
    def isPerfectSquare(self, num):
        i = 1

        while i * i < num:
            i += 1

        return i * i == num