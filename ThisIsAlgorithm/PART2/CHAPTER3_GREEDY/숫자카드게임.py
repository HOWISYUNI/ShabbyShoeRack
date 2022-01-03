def solution(row, col, image):
    answer = 0
    IDX = 1
    candidates = [min(vals) for vals in image]
    answer = max(candidates)

    return answer


if __name__ == '__main__':
    row, col = map(int, input().split())
    image = []
    for _ in range(row):
        image.append(list(map(int, input().split())))

    print(solution(row, col, image))