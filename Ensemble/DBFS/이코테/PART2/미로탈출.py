'''
풀이시간 : 30 분
시간 제한 : 1초
메모리 제한 : 128MB

괴물 위치 : 0
통로 : 1

* 배울 점
최단거리 계산
    1. dfs로 돌아가는 경로보다 bfs로 인접한 노드부터 보고 
    2. 각 노드를 처음 방문 했을 때 노드에 거리를 기록한다

'''

from collections import deque

def solution(n, m, graph):
    visited = [[False for _ in range(m)] for _ in range(n)]
    length = [[0 for _ in range(m)] for _ in range(n)]
    length[0][0] = 1

    # BFS
    q = deque()
    q.append((0, 0))

    # 상 하 좌 우 순서
    dxs = [-1, 1, 0, 0] 
    dys = [0, -0, -1, 1]
    
    # counts = []

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            # nx, ny가 유효한 위치고, 통로이며, 안가본 노드일 경우
            if isValid(nx, ny, n, m) and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True # 방문처리
                length[nx][ny] = length[x][y] + 1 # 인접 노드 까지의 거리 = 직전 노드까지의 거리 + 1 
                q.append((nx, ny))

    # dfs(0, 0, graph, visited, cnt, length, n, m) --> DFS로 풀 경우 탐색은 할 수 있지만, 랜덤탐색의 성격을 가져서 최단거리를 구하기엔 적합하지 않다.
    print(length)

    return length[n-1][m-1]

    


def dfs(x, y, graph, visited, cnt, length, n, m):
    print('DFS ENTER : ' + str(x) + ' / ' +str(y))

    visited[x][y] = True # 방문 처리
    cnt += 1
    length[x][y] = cnt
    
    # 상 하 좌 우 순서
    dxs = [-1, 1, 0, 0] 
    dys = [0, -0, -1, 1]

    # base : 출구에 도달했으면
    if x == n-1 and y == m-1:
        cnt += 1
        length[x][y] = cnt
        print('GOAL : ' + str(length[x][y]))
        return

    # dfs
    for dx, dy in zip(dxs, dys):
        # 유효하거나, 용이 없거나, 가보지 않았으면 탐색
        if isValid(x+dx, y+dy, n, m) and graph[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
            dfs(x+dx, y+dy, graph, visited, cnt, length, n, m)    

def isValid(x, y, m, n):
    if x >= 0 and y >= 0 and x < m and y < n:
        return True
    else:
        return False

if __name__ == '__main__':
    n, m = 5, 6
    graph = [
        [1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]
    ]

    print(solution(n, m, graph))