def turn_left(orientation):
    return 3 if orientation == 0 else orientation - 1

def valid(x, y, row_size, col_size):
    return 0 <= x < row_size and 0 <= y < col_size

def go_rear(x, y, orientation, DELTAS):
    orientation = abs(orientation - 2)
    dx, dy = DELTAS[orientation]
    nx, ny = x + dx, y + dy
    return nx, ny

def dfs(x, y, graph, orientation, row_size, col_size, visited):
    DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rotated = 0
    visited[x][y] = True

    # 반시계 방향으로 한 바퀴 돌아본다.
    while rotated < 4:
        orientation = turn_left(orientation)
        rotated += 1
        dx, dy = DELTAS[orientation]
        nx, ny = x + dx, y + dy

        # 안 가봤고, 바다가 아니며, 범위를 벗어나지 않았다면
        if not visited[nx][ny] and graph[nx][ny] != 1 and valid(nx, ny, row_size, col_size):
            dfs(nx, ny, graph, orientation, row_size, col_size, visited)


if __name__ == "__main__":
    import os

    with open(os.path.join(os.path.dirname(__file__),'tc1.txt'), mode='r') as f:
        lines = f.readlines()
        row_size, col_size = map(int, lines[0].strip().split())
        x, y, orientation = map(int, lines[1].strip().split())
        visited = [[False for _ in range(col_size)] for _ in range(row_size)]

        graph = []
        for i in range(2, 2 + row_size):
            graph.append(list(map(int, lines[i].strip().split())))

    dfs(x, y, graph, orientation, row_size, col_size, visited)

    # visited 에서 True를 세기
    cnt = 0
    for row in visited:
        for col in row:
            if col == True:
                cnt += 1

    print(cnt)