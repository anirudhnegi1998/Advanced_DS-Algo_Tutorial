from collections import defaultdict
class Solution:
    def traveller(self,row,column, memo={}):
        key = row,",",column
        if key in memo:
            return memo[key]
        if row == 1 and column ==1:
            return 1
        if row==0 or column ==0 :
            return 0
        memo[key] = self.traveller(row-1,column, memo) + self.traveller(row,column-1,memo)
        return memo[key]

s= Solution()
print(s.traveller(2,3))
