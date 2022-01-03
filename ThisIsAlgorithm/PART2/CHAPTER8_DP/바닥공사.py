
def solution(N):
    dp = [0 for _ in range(1_000)]

    dp[1] = 1
    dp[2] = 3

    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

    return dp[N]

if __name__ == '__main__':
    N = int(input())
    print(solution(N))