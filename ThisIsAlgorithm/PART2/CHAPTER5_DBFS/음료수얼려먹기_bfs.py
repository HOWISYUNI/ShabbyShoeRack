from collections import deque

def valid(x, y, row, col):
    return 0 <= x < row and 0<= y < col

def bfs(row, col, x, y, graph, visited):

    DELTAS = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy
            if valid(next_x, next_y, row, col) and not visited[next_x][next_y] and graph[x][y] == graph[next_x][next_y]:
                q.append((next_x, next_y))
                visited[next_x][next_y] = True # 방문했다.

if __name__ == "__main__":
    answer = 0
    row, col = map(int, input().split())
    graph = []

    for _ in range(row):
        graph.append(list(map(int,list(input()))))

    visited = [[False]*col for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if graph[x][y] == 0 and not visited[x][y]:
                visited[x][y] = True
                bfs(row, col, x, y, graph, visited)
                answer += 1

    print(answer)