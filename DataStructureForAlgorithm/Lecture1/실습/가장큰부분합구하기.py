import math

# divide and conquer를 활용한 풀이(O(NlogN), 90점)
def maxSubArray(nums):
    
    if len(nums) == 1:
        return nums[0]
        
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    
    # 경계값 포함
    
    # 좌측으로
    leftMax = -math.inf
    for i in range(mid, -1, -1):
        if sum(nums[i:mid]) > leftMax:
            leftMax = sum(nums[i:mid])
    # 우측으로
    rightMax = -math.inf
    for i in range(mid, len(nums)+1):
        if sum(nums[mid:i]) > rightMax:
            rightMax = sum(nums[mid:i])
            
    boundaryMax = leftMax + rightMax
    
    return max(maxSubArray(left), maxSubArray(right), boundaryMax)

# O(N) 풀이법. 문제의 nums 중 양수는 하나라도 존재한다는 조건 활용
def maxSubArray(nums): # O(N)의 풀이
    s = 0
    result = 0
    for i in nums:
        s += i
        result = max(s, result)
        if s < 0:
            s = 0

    return result

def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()