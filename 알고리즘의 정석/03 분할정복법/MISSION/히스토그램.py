import sys, math

def getRect(heights) :
    '''
    n개의 판자의 높이가 주어질 때, 이를 적당히 잘라 얻을 수 있는 직사각형의 최대 넓이를 반환하는 함수를 작성하세요.

    풀이 1 : divide and conquer(내가 푼 방식)
    풀이 2 : 세그먼트 트리 (https://www.acmicpc.net/blog/view/9)
    풀이 3 : 스택 (https://hooongs.tistory.com/330)
    '''
    
    # base condition
    if len(heights) == 1:
        return heights[0]
        
    mid = len(heights) // 2
    # 좌측, 우측   
    leftMax = getRect(heights[:mid])
    rightMax = getRect(heights[mid:])
    
    
    '''
    - 경계가 무조건 포함된 영역의 직사각형(경계가 포함되지 않은 경우는 위쪽 좌측, 우측 경우에 모두 포함됨)
    - 경계에서 좌우가 야금야금 넓어지는 방식
    1. 넓어지는 방향은 어디로 해도 상관없는데, 큰쪽으로 하면 얻어지는 큰 직사각형을 더 일찍 알아챈다는 것 밖에 없음. 어차피 연속부분 전체를 다 보고싶은데 기준 하나 세우는거임. 작은쪽으로 확장해도 전체 다 봄
    2. 확장한 방향의 높이와, 이전 높이랑 비교해서 더 작은 놈을 직사각형 높이라고 생각하고 계산
    3. 이전 넓이와 현재 넓이 중 큰놈을 계속 갱신함
    '''
    
    leftIdx, rightIdx = mid-1, mid
    boundaryHeight = min(heights[leftIdx], heights[rightIdx])
    boundaryMax = boundaryHeight*2
    
    while not (leftIdx == 0 and rightIdx == len(heights)-1):
    
        leftHeight = heights[leftIdx-1] if leftIdx != 0 else -math.inf
        rightHeight = heights[rightIdx+1] if rightIdx != len(heights)-1 else -math.inf
    
        if  leftHeight <= rightHeight:
            rightIdx += 1 if rightIdx < len(heights) else len(heights)-1
            boundaryHeight = min(boundaryHeight, rightHeight)
        else:
            leftIdx -= 1 if leftIdx > -1 else 0
            boundaryHeight = min(boundaryHeight, leftHeight)
            
            
        width = rightIdx - leftIdx + 1
        
        boundaryMax = max(boundaryMax, width*boundaryHeight)
        

    return max(leftMax, rightMax, boundaryMax)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getRect(data))

if __name__ == "__main__":
    main()
