class Solution:
    def fib_recursion(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


s = Solution() 
result = s.fib_recursion(10) 
print(result) 
