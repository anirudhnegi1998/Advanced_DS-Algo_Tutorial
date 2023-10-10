class Solution:
    def canSum(self,targetSum, numbers):
        ans= []
        help = []
        def helper(targetSum, numbers,ans,help):
            if targetSum == 0:
                ans.append(help)
                help=[]
                return ans
            if targetSum < 0:
                help=[]
                return ans
            for i in numbers:
                nextsum = targetSum - i
                help.append(i)
                helper(nextsum,numbers,ans,help)
            return ans
        return helper(targetSum, numbers,ans,help)


s = Solution()
print(s.canSum(7,[5,3,4,7]))