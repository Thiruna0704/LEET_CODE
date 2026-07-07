
class Solution(object):
    def minWindow(self, s, t):
        need = Counter(t)
        left = 0
        count = len(t)
        ans = ""

        for right in range(len(s)):
            if need[s[right]] > 0:
                count -= 1
            need[s[right]] -= 1

            while count == 0:
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right+1]

                need[s[left]] += 1
                if need[s[left]] > 0:
                    count += 1
                left += 1

        return ans