from collections import defaultdict
class Solution:
    def traveller(self,row,column,path=""):
        if row == 1 and column ==1:
            print("right path = ",path)
            return 1
        if row==0 or column ==0 :
            print("wrong path =",path)
            return 0
        return self.traveller(row-1,column,path+" down ") + self.traveller(row,column-1,path+" right ")

s= Solution()
print(s.traveller(2,3))
