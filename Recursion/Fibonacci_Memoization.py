class Solution:
    def __init__(self):
        self.cache = {}
    def fib_memoization(self,n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n<1:
            return 0
        if n==1 or n==2:
            return 1
        elif n>2:
            value = self.fib_memoization(n-1) + self.fib_memoization(n-2)
            self.cache[n] = value
            return value

s = Solution()
print(s.fib_memoization(10)) 