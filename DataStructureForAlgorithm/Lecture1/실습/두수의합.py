# 효율적이지 않은 코드
# def twoSum(nums, target):
#     for i in range(len(nums)-1):
#         a, b = nums[i], nums[i+1]
#         if a+b == target:
#             return a, b


# 째곰 더 효율적인 코드. 배열을 두번 돔
# def twoSum(nums, target):
#     for a in nums:
#         if target-a in nums:
#             return a, target-a

'''
효율적인 코드. 정렬하면 좀 더 효율적이다(시간복잡도도 그렇게 안크고)
정렬하면 배열을 한 번 밖에 안도니까 더 효율적이다
'''
def twoSum(nums, target):
    nums.sort() # 오름차순으로 정렬
    start, end = 0, len(nums)-1

    while start < end:
        sum = nums[start] + nums[end]
        
        if sum == target:
            return nums[start], nums[end]
        elif sum < target:
            start += 1
            continue
        else:  
            end -= 1
            continue
    

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
