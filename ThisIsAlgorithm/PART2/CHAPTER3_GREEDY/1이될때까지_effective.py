
def solution(n, k):
    answer = 0

    while True:
        if n == 1:
            break

        if n % k: # 나누어 떨어지지 않을 때
            # 나누어떨어지도록 나머지를 한번에 빼준다.
            remainder = n % k
            n -= (remainder)
            answer += (remainder)
            continue

        n = n // k
        answer += 1

    return answer

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))