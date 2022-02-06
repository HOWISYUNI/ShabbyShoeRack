'''
풀이시간 : 30분
시간 제한 : 1초
메모리제한 : 128MB

N X M 얼음 틀
구멍 : 0, 벽 : 1
이 얼음틀이 만들 수 있는 아이스크림 갯수 구하기
'''


def solution(n, m, graph):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for x in range(n): # 15
        for y in range(m): # 14
            if not visited[x][y] and graph[x][y] == 0: # 방문하지 않았고, 빈칸인 곳만 탐색
                # 탐색의 핵심 : 방문처리
                # dfs(x, y, graph, visited, n, m)
                bfs(x, y, graph, visited, n, m)
                cnt += 1

    return cnt

def dfs(x, y, graph, visited, n, m):

    # base condition : 벽이거나, 방문한위치거나, 유효한 위치가 아니면 탐색 중단
    if not isValid(x, y, n, m) or graph[x][y] == 1 or visited[x][y] :
        return

    # 방문처리
    visited[x][y] = True

    dfs(x-1, y, graph, visited, n, m) # 상
    dfs(x+1, y, graph, visited, n, m) # 하
    dfs(x, y-1, graph, visited, n ,m) # 좌
    dfs(x, y+1, graph, visited, n, m) # 우

def isValid(x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    else:
        return True


from collections import deque

def bfs(x, y, graph, visited, n, m):
    q = deque()
    q.append((x, y))
    dxs = [1, -1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        visited[x][y] = True # 방문처리
        for dx, dy in zip(dxs, dys): # 상하좌우 검색
            if isValid(x+dx, y+dy, n, m) and graph[x+dx][y+dy] == 0 and not visited[x+dx][y+dy]: # 유효한 위치고, 빈칸이고, 안가봤으면 탐색
                q.append((x+dx, y+dy))

if __name__ == "__main__":
    n, m = 15, 14
    graph = [
        [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
        [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
        [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
        [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
        [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
        [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
    ]
    print(solution(n, m, graph))
