n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])

# 4
# 1 5 6 7 
# 1  2  3  4 