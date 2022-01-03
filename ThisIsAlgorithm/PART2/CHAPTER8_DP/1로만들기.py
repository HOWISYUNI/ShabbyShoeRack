def solution(N):
    # dp table
    dp = [0 for _ in range(30_000)]

    # bottom up
    for i in range(2, N + 1):
        # 후보군 선정
        a = i // 5 if i % 5 == 0 else -1
        b = i // 3 if i % 3 == 0 else -1
        c = i // 2 if i % 2 == 0 else -1
        d = i - 1

        candidates = [a, b, c, d]
        candidates = [candidate for candidate in candidates if candidate != -1]

        # 후보군 중 최소 연산량인 후보값 찾기
        val_candidates = [dp[candidate] for candidate in candidates]
        min_val = min(val_candidates)

        # 최소 연산량 + 1 이 dp 테이블 값
        dp[i] = min_val + 1

    return dp[N]

if __name__ == '__main__':
    N = int(input())
    print(solution(N))