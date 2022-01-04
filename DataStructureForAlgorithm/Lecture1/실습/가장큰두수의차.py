# 배열 다 도는것보다 째끔 효율적인 코드
# def maxTwoDiff(nums):
#     nums.sort()
#     return nums[-1]-nums[0]

'''
시간복잡도 : 정렬보다 min, max가 낫다
정렬 : O(NlogN)
min, max : O(N)
'''

def maxTwoDiff(nums):
    return max(nums)-min(nums)

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
