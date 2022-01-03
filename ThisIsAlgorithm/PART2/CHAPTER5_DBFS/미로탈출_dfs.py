def dfs(x, y, row, col, image, visited, cur_dist, distances):
    visited[x][y] = True
    cur_dist += 1
    DELTAS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    if x == row - 1 and y == col - 1:
        distances.append(cur_dist)

    for dx, dy in DELTAS:
        next_x = x + dx
        next_y = y + dy
        if valid(next_x, next_y, row, col) and not visited[next_x][next_y] and image[next_x][next_y] == 1:
            dfs(next_x, next_y, row, col, image, visited, cur_dist, distances)

def valid(x, y, row, col):
    return 0 <= x < row and 0 <= y < col

if __name__ == '__main__':
    row, col = 5, 6
    image = [[1, 0, 1, 0, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1]]

    visited = [[False]*col for _ in range(row)]
    answer = 0

    distances = []
    cur_dist = 0

    dfs(0, 0, row, col, image, visited, cur_dist, distances)

    print(min(distances))