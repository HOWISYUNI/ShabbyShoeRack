import os

def turn_left(direction):
    if direction == 0:
        return 3
    else:
        return direction - 1

def valid(nx, ny, row_size, col_size):
    return 0 <= nx < row_size, 0 <= ny < col_size

def go_rear(x, y, graph, direction, DELTAS):
    # direction = abs(direction - 2)
    dx, dy = DELTAS[direction]
    nx, ny = x - dx, y - dy  # delta를 빼면 뒤로 돌아간다.
    
    return (nx, ny)

def solution(graph, x, y, direction, row_size, col_size):
    start_x, start_y = x, y
    NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    visited[x][y] = True

    DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cnt = 1  # 시작한 부분도 한번 방문해본것과 같으니까
    rotated = 0

    while True:
        direction = turn_left(direction)
        dx, dy = DELTAS[direction]
        nx = x + dx
        ny = y + dy
        
        # 아직 가보지 않은 방향이고 범위 안에 있으며 바다가 아닐 때 가본다
        if not visited[nx][ny] and graph[nx][ny] != 1 and valid(nx, ny, row_size, col_size):
            x = nx
            y = ny
            visited[x][y] = True  # 가본다
            cnt += 1
            rotated = 0
            continue
        else: # 못간다면 회전만 한다.
            rotated += 1

        # 다 돌아봤는데 못간다면(다 가본데거나 바다거나)
        if rotated == 4:
            # 뒤로 돌아온다.
            x, y = go_rear(x, y, graph, direction, DELTAS)
            rotated = 0  # x, y가 변하면 항상 rotated 는 초기화
            if graph[x][y] == 1: # 뒤가 바다라면 리턴
                return cnt


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__),'tc1.txt'), mode='r') as f:
        lines = f.readlines()
        row_size, col_size = map(int, lines[0].strip().split())
        x, y, direction = map(int, lines[1].strip().split())

        graph = []
        for i in range(2, 2 + row_size):
            graph.append(list(map(int, lines[i].strip().split())))

    
    print(solution(graph, x, y, direction, row_size, col_size))