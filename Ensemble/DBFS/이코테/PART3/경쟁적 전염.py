'''
난이도 : **
풀이 시간 : 50분
시간 제한 : 1초
메모리 제한 : 256MB

N x N 그래프
1 ~ K 종류 바이러스
S 초 동안 전염
    1 초에 1 ~ K 바이러스 순으로 전염

전염 후 (X, Y)에 존재하는 바이러스 종류 출력 (전염 안됐으면 0)

'''

def solution(N, K, graph, S, X, Y):
    # 바이러스 위치 파악
    virusPosition = [[] for _ in range(K+1)] # 1번 바이러스는 virusePosition[1] 리스트에 존재
    for row in range(N):
        for col in range(N):
            if graph[row][col] != 0:
                virusType = graph[row][col]
                virusPosition[virusType].append((row, col))

    # 초단위로 반복 : 1 ~ S
    for sec in range(S):
        # 1 ~ K 순서로 DBFS. 탐색 후 현재 탐색에서 다음 전염 노드 리스트를 반환
        for type in range(1, K+1):
            virusPosition[type] = bfs(N, graph, type, virusPosition) # 타입 별 바이러스 위치를 갱신

    return graph[X-1][Y-1] # (X, Y) 위치의 바이러스 종류 출력

from collections import deque

def bfs(N, graph, type, virusPosition):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    nextIterVirus = []

    q = deque(virusPosition[type])

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = cx+dx
            ny = cy+dy
            if isValid(nx, ny, N) and graph[nx][ny] == 0: # 유효하고, 어느 바이러스도 전염되지 않은 위치라면
                graph[nx][ny] = type
                nextIterVirus.append((nx, ny))

    return nextIterVirus

def isValid(x, y, N):
    return 0 <= x < N and 0<= y < N


if __name__ == "__main__":
    # case 1
    N, K = 3, 3
    graph = [
        [1,0,2],
        [0,0,0],
        [3,0,0]
    ]
    S, X, Y = 2,3,2

    # case 2
    S, X, Y = 1,2,2

    print(solution(N, K, graph, S, X, Y))