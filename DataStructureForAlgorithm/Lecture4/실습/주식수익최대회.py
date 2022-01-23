
'''
주식 수익 최대화
주식 가격을 나타내는 숫자들의 배열이 주어집니다. 즉, 배열의 인덱스 i의 숫자가 해당 시간의 주식 가격입니다.

주식 한 주를 단 한번 사고 단 한번 팔 수 있다고 합시다. 이때 최대 수익을 구해내는 알고리즘을 구현 해 보세요.

예를 들어서,

1, 2, 3, 4, 5, 6, 7 과 같은 경우엔 1일때 사서 7일때 파는게 가장 이득입니다. 따라서 6을 반환하면 됩니다.

7, 6, 5, 4, 3, 2, 1 과 같은 경우에는 주식 가격이 쭉 하락했으므로, 이득을 낼 수 없습니다. 0을 반환하면 됩니다.

1, 2, 3, 4, 3, 2, 1 과 같은 경우엔 1일때 사서 4일때 파는게 가장 이득입니다. 3을 반환하면 됩니다.

2, 8, 19, 37, 4, 5 와 같은 경우엔 2일때 사서 37일때 파는게 가장 이득입니다. 35를 반환하면 됩니다.
'''

import math
def maximizeProfit(nums):
    # 완전탐색으로 풀 경우 시간 초과
#     maxVal = -math.inf
    
#     for start in range(len(nums)-1):
#         for end in range(start+1, len(nums)):
#             tempVal = nums[end] - nums[start]
#             if tempVal > maxVal:
#                 maxVal = tempVal
                
#     return maxVal if maxVal > 0 else 0


    # divide and conquer 도 시간초과
    
#     # base
#     if len(nums) == 1:
#         return 0
#     if len(nums) == 2:
#         return nums[1] - nums[0] if nums[1] - nums[0] > 0 else 0

    
#     # Recursion
#     mid = len(nums)//2
#     left = maximizeProfit(nums[:mid])
#     right = maximizeProfit(nums[mid:])
    
#     # 경계포함 범위 내 최대 수익
    
#     ## 왼쪽 최저 점,최대 수익을 찾아감
#     leftPoint, leftBoundaryMax = mid-1, 0
#     for i in range(mid-1,-1, -1):
#         if nums[mid-1]-nums[i] > 0 and nums[mid-1]-nums[i] > leftBoundaryMax:
#             leftBoundaryMax = nums[mid-1]-nums[i]
#             leftPoint = i
#             # print('temp leftPoint : ' + str(leftPoint)) # DEBUG
    
#     ## 오른쪽 최고점, 최대 수익을 찾아감
#     rightPoint, rightBoundaryMax = mid, 0
#     for i in range(mid, len(nums)):
#         if nums[i]-nums[mid] > 0 and nums[i]-nums[mid] > rightBoundaryMax :
#             rightBoundaryMax = nums[i]-nums[mid]
#             rightPoint = i
#             print(nums[i], nums[mid])
#             # print('temp rightPoint : ' + str(rightPoint)) # DEBUG
    
#     # 왼쪽 최저점, 오른쪽 최대점 간 수익 계산
#     left2rightMax = nums[rightPoint]-nums[leftPoint] if nums[rightPoint]-nums[leftPoint] > 0 else 0
    
    
#     ## DEBUG
#     # print('------------nums : ' + str(nums))
#     # print('----- left : ' + str(left))
#     # print('----- right : ' + str(right))
#     # print('----- left point : ' + str(leftPoint) + '/ right point : ' + str(rightPoint))
#     # print('----- leftBmax : ' + str(leftBoundaryMax) + '/ rightBMax : ' + str(rightBoundaryMax) + '/ left2rightMax : ' + str(left2rightMax))
#     # print('= FINAL MAX : ' + str(max(left, right, leftBoundaryMax, rightBoundaryMax, left2rightMax)))
    
#     return max(left, right, leftBoundaryMax, rightBoundaryMax, left2rightMax)
        

    # 정답 O(N) 풀이. O(N^2), O(NlogN)이 틀렸다면 O(N)의 알고리즘으로 풀어야한다.
    '''
    최대값 찾기 문제 : 최대값을 갱신하면서 찾는다.
    1. maxProfit을 갱신한다 : 기존 최대값과 이번 계산값을 비교하면서 더 큰값을 기억한다. 
    2. minVal을 갱신한다. 최저점을 기억해야 최대수익을 낼 수 있다
    '''
    minVal, maxVal = math.inf, -math.inf
    maxProfit = 0
    risingCnt = 0
    
    for curVal in nums:
        maxProfit = max(maxProfit, curVal - minVal) # 최대이익 갱신되면 갱신한다. 하락장이면 cur-min 이 항상 음수니까 maxProfit 고대로
        minVal = min(minVal, curVal) # 다음번 iteration의 최대수익(curVal-minVal) 위해 minVal 갱신
        
    return maxProfit
    

def main():
    print(maximizeProfit([1,2,3,4,5,6,7])) # 6
    print(maximizeProfit([7,6,5,4,3,2,1])) # 0
    print(maximizeProfit([1,2,3,4,3,2,1])) # 3
    print(maximizeProfit([2,8,19,37,1,37])) # 35

if __name__ == "__main__":
    main()