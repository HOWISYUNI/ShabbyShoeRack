import sys, math

def calcDistance(p1, p2):

    X, Y = 0, 1
    
    return (p1[X]-p2[X])**2 + (p1[Y]-p2[Y])**2

def getDist(points) :
    '''
    n개의 점이 주어질 때, 가장 가까운 두 점 사이의 거리의 제곱을 반환하는 함수를 작성하세요.

    예를 들어, 점이 4개가 있고, 각각의 좌표가 (0, 3), (1, 1), (2, 2), (7, 1) 이라면 points에는 다음과 같이 그 정보가 저장됩니다.

    points = [ (0, 3), (1, 1), (2, 2), (7, 1) ]

    이 때, 가장 가까운 두 점 사이의 거리의 제곱은 2입니다.
    '''
    
    result = math.inf

    # loop 돌면서 모든 점 2쌍을 찾고 최단거리 갱신 갱신
    for idx1 in range(len(points)):
        for idx2 in range(idx1+1, len(points)):
            distance = calcDistance(points[idx1], points[idx2])
            
            result = min(result, distance)
    
    return result

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print(getDist(points))

if __name__ == "__main__":
    main()
