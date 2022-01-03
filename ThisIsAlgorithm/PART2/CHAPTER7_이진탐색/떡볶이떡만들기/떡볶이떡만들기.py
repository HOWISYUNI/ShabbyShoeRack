def cut(ddocks, mid):
    # mid 만큼 잘라도 남으면 리스트에 기록
    return sum([ddock - mid if ddock - mid >= 0 else 0 for ddock in ddocks])


def solution(counts, goal, ddocks):

    end = max(ddocks) # 가장 긴떡
    start = 0

    while start <= end:
        mid = (start + end) // 2  # mid 길이만큼 자른다
        remainder = cut(ddocks, mid) # mid 만큼 자르고 남은 길이

        if remainder > goal:
            start = mid + 1
            continue
        elif remainder < goal:
            end = mid - 1
            continue
        elif remainder == goal:
            return mid

    if start > end:
        return mid


if __name__ == "__main__":
    import os 
    with open(os.path.join(os.path.dirname(__file__), 'tc1.txt'), mode='r') as f:
        lines = f.readlines()
        counts, goal = map(int, lines[0].strip().split())
        ddocks = list(map(int, lines[1].strip().split()))
        ddocks.sort()

    print(solution(counts, goal, ddocks))