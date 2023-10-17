class Solution:
    def reverse(self,s):
        if not s:
            return None
        ans = 0
        def helper(s,ans):
            if s<1:
                return ans
            ans = s%10+ans*10
            return(helper(s//10,ans))
        return (helper(s,ans))

s = Solution()
print(s.reverse(2345))