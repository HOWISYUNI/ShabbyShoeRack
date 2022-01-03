from collections import deque

def valid(x, y, row, col):
    return 0 <= x < row and 0 <= y < col

def bfs(x, y, row, col, graph, visited):
    cnts = []
    q = deque()
    q.append((x,y))
    DELTAS = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in DELTAS:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if valid(next_x, next_y, row, col) and not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                q.append((next_x, next_y))
                visited[next_x][next_y] = True
                graph[next_x][next_y] = graph[cur_x][cur_y] + 1

    return graph[row - 1][col - 1]


if __name__ == '__main__':
    row, col = map(int, input().split())
    graph = []
    visited = [[False]*col for _ in range(row)]

    for x in range(row):
            graph.append(list(map(int, input())))

    visited[0][0] = True
    print(bfs(0, 0, row, col, graph, visited))