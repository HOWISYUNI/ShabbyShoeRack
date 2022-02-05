'''
N x M 직사각형 맵
각 칸은 육지(0) 또는 바다(1)

캐릭터
    1. 이동 : 상 하 좌 우
    2. 방향 : 북(0), 동(1), 남(2), 서(3)

제한조건
    1. 첫 위치는 항상 육지
    2. 바다는 갈 수 없다
    3. 맵 외곽은 항상 바다

이동조건
    1. 현재 위치, 방향 기준 왼쪽방향(시계반시계, 90도)을 보면서 갈 곳 정한다
        1. 아직 가보지 않은 칸 : 왼쪽방향으로 회전 -> 전진
        2. 가본 칸 or 바다 : 왼쪽 방향으로 회전
        3. 모두 가본 칸 or 모두 바다 = 모두 갈 수 없다: 방향유지
            1. 뒤가 육지 : 뒤로 한 칸
            2. 뒤가 바다 : 정지

처음 슈도코드 개념으로 짜기 시작할때는 변수 많이 도입하는게 깔끔한데
실제 구현하면서 position이 개념이 많아지면 pos 변수보다 dx, dy, nx, ny 변수로 처리해야 코드가 깔끔하다
'''
from collections import deque
from os import curdir
from turtle import backward

def solution(rowSize, colSize, posX, posY, curDirection, matrix):
    cnt = 0
    visited = [[False for _ in range(colSize)] for _ in range(rowSize)] # 가봤다 True, 안가봤다 False
    visited[posX][posY] == True # 시작지점은 항상 가봤다
    GROUND, SEA = 0, 1
    X, Y = 0, 1
    forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = deque()
    q.append((posX, posY))
    
    while q:
        curPos = q.popleft()
        print("curpos : " + str(curPos)) 

        # turn left
        for nextDirection in getNextDirection(curDirection):
            nx = curPos[X]+forward[nextDirection][X]
            ny = curPos[Y]+forward[nextDirection][Y]
            print("nextpos : " + str((nx, ny)) + "/ next Direction : " + str(nextDirection))
            
            if not visited[nx][ny] and matrix[nx][ny] == GROUND: # 안가봤고 육지면
                # 회전하고
                curDirection = nextDirection
                # 전진한다
                print("GO " + str((nx, ny)) + " / " + str(nextDirection) + " direction")
                q.append((nx, ny))

                visited[nx][ny] = True
                cnt += 1
                break
            
            else: # 가본칸이거나 바다거나
                # 회전만 한다
                curDirection = nextDirection

        else: # 다 가본칸이거나 다 바다거나
            bx, by = getBackwardPos(curPos, curDirection)

            if matrix[bx][by] == GROUND: # 뒤가 육지면
                print("BACK")
                curPos = (bx, by)
                q.append((bx, by)) # 이전 지점의 사방을 다 못보고 왔을수도 있으니깐 뒤로가서 다시 탐색한다
            else: # 뒤가 바다면
                print("STOP")
                return cnt

def getNextDirection(curDirection):
    result = []

    for _ in range(4):
        if curDirection == 0:
            result.append(3)
            curDirection = 3
        else:  
            result.append(curDirection-1)
            curDirection = curDirection-1
    else:
        return result
        

def getBackwardPos(curPos, curDirection):
    NORTH, EAST, SOUTH, WEST = 0, 1 ,2, 3
    backward = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    X, Y = 0, 1

    for i in range(4):
        if curDirection == i:
            backwardPos = (curPos[X]+backward[i][X], curPos[Y]+backward[i][Y])

    return backwardPos


if __name__ == '__main__':
    # N, M = map(int, input().split())
    # posX, posY, direction = map(int, input().split())

    # matrix = []
    # for _ in range(N):
    #     matrix.append(list(map(int, input().split())))

    N, M = 4, 4
    posX, posY, direction = 1, 1, 0
    matrix = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

    print(solution(N, M, posX, posY, direction, matrix))