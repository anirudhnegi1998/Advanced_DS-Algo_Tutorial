class Solution:
    def list_prime(self,n):
        true_list = [True for i in range(n+1)]
        i = 2
        while i*i <=n:
            if true_list[i]:
                for p in range(i*i,n+1,i):
                    true_list[p] = False
            i+=1
        
        ans=[]
        for i in range(2,n+1,1):
            if true_list[i]:
                ans.append(i)
        return ans

s= Solution()
print(s.list_prime(10))