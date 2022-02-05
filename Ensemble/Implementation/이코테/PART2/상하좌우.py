from unicodedata import name


def solution(N, plans):

    X, Y = 0, 1
    moveTypes = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    curPos = (1, 1)
    
    for direction in plans:
        # nextPos 구하기
        for idx in range(len(moveTypes)):
            if direction == moveTypes[idx]:
                nextPos = (curPos[X]+dx[idx], curPos[Y]+dy[idx])

        # nextPos 갱신
        if isValid(nextPos, N):
            curPos = nextPos

    return str(curPos[X]) + ' ' + str(curPos[Y])


def isValid(pos, size):
    X, Y = 0, 1

    if pos[X] == 0 or pos[Y] == 0:
        result = False
    elif pos[X] > size or pos[Y] > size:
        result = False
    else:
        result = True

    return result
        


if __name__ == "__main__":
    # N = int(input())
    # plans = input().split()

    N = 5
    plans = ['R', 'R', 'R', 'U', 'D', 'D']

    print(solution(N, plans))