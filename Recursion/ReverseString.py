class Solution:
    def reverse(self,s):
        if not s:
            return None
        start = 0
        n = len(s)
        def helper(s,start,n):
            if start>=n-1:
                return s[start]
            ans = helper(s,start+1,n)+s[start]
            return ans
        return(helper(s,start,n))

s = Solution()
print(s.reverse("ABC"))


