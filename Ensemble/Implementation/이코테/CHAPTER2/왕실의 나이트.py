'''
8x8 좌표평면상 임의의 점에서 나이트가 이동할 수 있는 경우의 수를 출력하라
나이트는 L자 형태, 두 가지 경우의 수로 이동할 수 있다.
1. 수평 2칸 수직 1칸
2. 수평 1칸 수직 2칸

행 위치는 1 ~ 8, 열 위치는 a ~ h로 표현한다

시간제한 1초
메모리 제한 128MB
'''

def solution(pos):

    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    # steps = [(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)] 로 구현해도됨ㄴ
    X, Y = 0, 1
    cnt = 0

    # 현재 위치 숫자로 변환
    curPos = (ord(pos[X])-96, int(pos[Y]))

    # check
    for i in range(len(dx)):
        nextPos = (curPos[X]+dx[i], curPos[Y]+dy[i])
        if isValid(nextPos):
            cnt += 1

    return cnt

def isValid(pos):
    X, Y = 0, 1

    if pos[X] < 1 or pos[Y] < 1:
        result = False
    elif pos[X] > 8 or pos[Y] > 8:
        result = False
    else:
        result = True

    return result

if __name__ == '__main__':
    # pos = input()
    pos = 'a1'

    print(solution(pos))