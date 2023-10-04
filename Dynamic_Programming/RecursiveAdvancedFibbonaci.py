from collections import defaultdict

class Solution:
    def fib(self,n, memo=defaultdict(int)):
        if n in memo:
            return memo[n]
        if n ==0:
            return 0
        if n==1 or n==2:
            return 1
        memo[n] = self.fib(n-2) + self.fib(n-1)
        return memo[n]

s= Solution()
print(s.fib(10))