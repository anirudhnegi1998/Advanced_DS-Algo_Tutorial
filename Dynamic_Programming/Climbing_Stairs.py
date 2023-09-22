class Solution:
    def stairs(self, n) -> int:
        ans = {}
        ans[1] = 1
        ans[2] = 2
        for i in range(3,n+1):
            ans[i] = ans[i-2] + ans[i-1]
        return ans[n]

s = Solution()
print(s.stairs(5))