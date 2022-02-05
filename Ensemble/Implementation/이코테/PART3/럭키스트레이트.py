'''
풀이시간 : 20분
시간제한 : 1초
메모리제한 256MB

N을 자리수 기준으로 반 나눔
1. 좌측 반 자릿수 합 == 우측 반 자릿수 합
    LUCKY
2. ELSE : !=
    READY
'''

def solution(inputVal):
    mid = len(inputVal)//2
    left, right = inputVal[:mid], inputVal[mid:]

    leftSum, rightSum = 0, 0

    for i in left:
        leftSum += int(i)

    for i in right:
        rightSum += int(i)

    if leftSum == rightSum:
        return "LUCKY"
    else:
        return "READY"

if __name__ == '__main__':
    # inputVal = '123402'
    inputVal = '7755'
    print(solution(inputVal))