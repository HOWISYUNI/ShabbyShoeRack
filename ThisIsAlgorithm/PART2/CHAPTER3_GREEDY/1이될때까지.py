
def solution(n, k):
    answer = 0

    while True:
        if n == 1:
            break

        if n % k: # 나누어 떨어지지 않을 때
            n -= 1
            answer += 1
            continue

        n = n // k
        answer += 1

    return answer

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))