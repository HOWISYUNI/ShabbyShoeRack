'''
숫자들의 배열이 주어지고 표적 숫자가 주어졌다고 합시다. 배열에 주어진 숫자들 중 두 개의 숫자를 더하면 표적 숫자가 되는데요, 이때 어떤 두 수를 더하면 표적숫자가 되는지 찾는 문제를 풀어 봅시다.예를 들어서, [2, 8, 19, 37, 4, 5] 가 배열로 주어지고 12 가 표적으로 주어지면 8,4 를 찾아내시면 됩니다.

입력 배열에는 중복되는 수가 없습니다.
입력 배열에는 합해서 표적이 되는 어떤 두 수가 반드시 있습니다.
출력의 순서는 상관 없습니다. 위 예시의 경우, 8,4 와 4,8은 둘 다 정답으로 인정합니다.
수수께끼 같은 느낌도 들죠? 코드의 효율성도 채점합니다. 100점에 도전 해 보세요!
100점을 못 받더라도 걱정하지 마세요. 해당 강의를 다 듣고 나면 100점을 받을 수 있습니다.
'''

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
