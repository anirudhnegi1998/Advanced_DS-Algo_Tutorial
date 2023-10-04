from collections import defaultdict 
class Solution:
    def fib(self,n):
        map= defaultdict(int)
        map[1] = 1
        map[2] = 1
        for i in range(3,n+1):
            map[i] = map[i-1]+map[i-2]
        return map[n]


s = Solution() 
result = s.fib(10) 
print(result) 
