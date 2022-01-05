import math

# divide and conquer를 활용한 풀이(90점)
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

def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()