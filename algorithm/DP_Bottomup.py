# 보텀업 방식은 타블레이션(tabulation)을 사용하여 다이나믹 프로그래밍을 구현하는 방식 중 하나이다.
# 타블레이션(tabulation)이란 하위 문제부터 천천히 해결하면서 더 큰 문제를 해결하는 기법을 말한다.
# 타블레이션이라고 부르는 이유는 작은 문제부터 큰 문제까지 하나하나 테이블을 채워간다는 의미 때문이다. 보텀업 방식은 하위 문제부터 시작해서 더 큰 문제를 해결해 나가기 때문에 상향식이라고도 한다.
# 다이나믹 프로그래밍의 전형적인 형태는 바로 이 보텀업 방식이다.
# 보텀업방식은 반복문을 이용하여 구현할 수 있다.


# 작은 문제부터 해결해서 저장할 dp테이블
dp = [0]*100

# fibo(1) = fibo(2) = 0
dp[1] = 1
dp[2] = 1
n = 99

# 피보나치 수열을 반복문으로 구현(bottom up)
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])