def solution(input_size, limitation, continuous, candidates):
    answer = 0
    candidates.sort()

    # 가장 큰 수 연속 continous번 + 다음 큰 수 1번 이 반복됨을 찾아야한다.
    first = candidates[-1]
    second = candidates[-2]
    one_unit = first*continuous + second
    max_loop, remainder = limitation//(continuous+1), limitation%(continuous+1)

    answer = one_unit*max_loop + first*remainder

    return answer


if __name__ == '__main__':
    input_size, limitation, continuous = map(int, input().split())
    candidates = list(map(int, input().split()))

    print(solution(input_size, limitation, continuous, candidates))
