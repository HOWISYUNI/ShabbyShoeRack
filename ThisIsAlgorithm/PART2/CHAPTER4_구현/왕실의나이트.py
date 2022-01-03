
def valid(nx, ny):
    return 1 <= nx <= 8 and 1 <= ny <= 8

def solution(row, col):
    row = int(row)
    col = ord(col) - 96
    cnt = 0

    DELTAS = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    for dx, dy in DELTAS:
        nx = row + dx
        ny = col + dy
        if valid(nx, ny):
            cnt += 1

    return cnt

if __name__ == "__main__":
    col, row = input()
    print(solution(row, col))