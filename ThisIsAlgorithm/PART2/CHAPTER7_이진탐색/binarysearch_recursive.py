def binsearch(arr, start, end, target):

    # 종결조건
    if start >= end:
        return -1

    mid = (start + end) // 2

    if target < arr[mid]:
        end = mid - 1
        return binsearch(arr, start, end, target)
    elif arr[mid] < target:
        start = mid + 1
        return binsearch(arr, start, end, target)
    else:
        return mid

if __name__ == "__main__":
    arr = [18, 0, 2, 16, 6, 8, 14, 12, 10, 4]

    arr.sort()
    print(binsearch(arr, start=0, end=len(arr), target=5))