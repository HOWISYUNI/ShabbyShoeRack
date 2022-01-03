def binsearch(arr, start, end, target):

    while start <= end:  # start < end 라면 찾고자 하는 대상이 arr[end] 일 때 못찾는다.
        mid = (start + end) // 2

        if target < arr[mid]:
            end = mid - 1
            continue
        elif arr[mid] < target:
            start = mid + 1
            continue
        else:
            return mid

    if start > end:  # 
        return -1

if __name__ == "__main__":
    arr = [18, 0, 2, 16, 6, 8, 14, 12, 10, 4]

    arr.sort()
    print(binsearch(arr, start=0, end=len(arr), target=4))