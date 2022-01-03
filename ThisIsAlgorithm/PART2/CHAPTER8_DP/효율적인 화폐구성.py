
def solution(goal, coins):
    dp = [0 for _ in range(10_000 + 1)]

    dp[0] = 0
    min_coin = min(coins)
    for i in range(1, min_coin):
        dp[i] = -1

    for i in range(min_coin, goal + 1):
        """
        1. 기본 논리 : 최솟값이 최솟값을 만든다.
        2. 중복방지 최소 단위 : 가늫한 코인. 원하는 값(i) = 가능한 코인(coin) + 나머지 값(remainder) 로 중복없이 셀 수 있음
        """
        available_coins = [coin for coin in coins if coin <= i]
        # 가능한 코인 중 가능한 조합
        remainders = [i - coin for coin in available_coins]
        candidates = [dp[remainder] + 1 for remainder in remainders if dp[remainder] != -1]

        # 가능한 조합 중 dp 최솟값
        dp[i] = min(candidates) if candidates else -1

    return dp[goal]


if __name__ == '__main__':
    N, goal = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    print(solution(goal, coins))