import sys

MAX = 1000000
dp = [1] * (MAX+1)
memo = [0] * (MAX+1)
ans = []

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
        dp[i*j] += i
        j += 1
        
for i in range(1, MAX+1):
    memo[i] = memo[i-1] + dp[i]
    
n = int(sys.stdin.readline())
for _ in range(n):
    data = int(sys.stdin.readline())
    ans.append(memo[data])

print('\n'.join(map(str,ans)))