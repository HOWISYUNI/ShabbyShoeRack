def dfs(x, y, row, col, image, visited):
    visited[x][y] = True
    DELTAS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for dx, dy in DELTAS:
        next_x = x + dx
        next_y = y + dy
        if valid(next_x, next_y, row, col) and not visited[next_x][next_y] and image[next_x][next_y] == 0:
            dfs(next_x, next_y, row, col, image, visited)

def valid(x, y, row, col):
    return 0 <= x < row and 0 <= y < col

if __name__ == '__main__':
    row, col = 4, 5
    image = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1],[1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

    visited = [[False]*col for _ in range(row)]
    answer = 0

    for x in range(row):
        for y in range(col):
            if image[x][y] == 0 and not visited[x][y]:
                dfs(x, y, row, col, image, visited)
                answer += 1

    print(answer)