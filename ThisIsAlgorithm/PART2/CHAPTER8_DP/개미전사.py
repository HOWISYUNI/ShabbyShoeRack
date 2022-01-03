
def solution(N, warehouse):
    dp = [0 for _ in range(100 + 1)]

    dp[0] = warehouse[0]
    dp[1] = max(dp[0], warehouse[1])

    for i in range(2, N):
        """
        1. 기본 아이디어 : 최댓값을 누적해야 최댓값을 구한다.
        2. 분기 최소 단위 : 인접(i-1)한 원소 vs 한 칸 이상 떨어진(i-2) 원소 
        """
        nearby = dp[i - 1]
        pongdang = dp[i - 2] + warehouse[i]
        dp[i] = max(nearby, pongdang)  # 직전 식량만 먹을것인가, 한칸 띄워서 2개를 먹을것인가

    return dp[N - 1]


if __name__ == '__main__':
    N = int(input())
    warehouse = list(map(int, input().split()))

    print(solution(N, warehouse))
