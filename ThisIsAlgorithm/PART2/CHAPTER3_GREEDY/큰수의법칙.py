def solution(input_size, limitation, continuous, candidates):
    candidates.sort()

    answer = 0
    iteration = 0

    for _ in range(limitation):
        max_value = candidates[-1]

        if iteration >= continuous:
            answer += candidates[-2]
            iteration = 0
            continue

        answer += max_value
        iteration += 1

    return answer


if __name__ == '__main__':
    input_size, limitation, continuous = map(int, input().split())
    candidates = list(map(int, input().split()))

    print(solution(input_size, limitation, continuous, candidates))



