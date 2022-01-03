def solution(item_count, items, target_count, targets):
    for target in targets:
        result = binary_search(arr=items, target=target, start=0, end=item_count - 1)
        
        print('no' if result == -1 else 'yes', end=' ')

def binary_search(arr, target, start, end):
    # start == end 를 확인해야 start == mid == end가 되어 마지막 하나의 원소까지 확인할 수 있다.
    # start == mid == end 일 때 도 못찾으면 end = mid - 1 이나 start = mid + 1이 되어 start > end 역전 현상으로 못찾음을 티낼 수 있다.
    while start <= end:  
        mid = (start + end) // 2

        if target < arr[mid]:
            end = mid -1
            continue
        elif arr[mid] < target:
            start = mid + 1
            continue
        else:  # arr[mid] == target
            return mid

    if start > end:  # end가 작아졌든 start가 커졌든 해서 start > end 역전 현상이 벌어졌다.
        return -1

if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), 'tc2.txt'), mode='r') as f:
        lines = f.readlines()
        item_count = int(lines[0])
        items = list(map(int, lines[1].split()))  
        items.sort()  # 정렬해야지만 이진탐색을 사용할 수 있다.
        target_count = int(lines[2])
        targets = list(map(int, lines[3].split()))

    solution(item_count, items, target_count, targets)