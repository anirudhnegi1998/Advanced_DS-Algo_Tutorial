class Solution:
    def canSum(self,targetSum, numbers):
        if targetSum ==0:
            return True
        if targetSum <0:
            return False
        
        for i in numbers:
            newtarget = targetSum - i
            if(self.canSum(newtarget,numbers) == True):
                return True
        
        return False

s = Solution()
print(s.canSum(7,[5,3,4,7]))