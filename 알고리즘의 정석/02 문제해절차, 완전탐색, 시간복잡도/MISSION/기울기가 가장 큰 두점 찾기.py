import sys, math

def getGradient(p1, p2):
    X, Y = 0, 1
    return abs((p1[Y]-p2[Y])/(p1[X]-p2[X]))

def maxSlope(points) :
    '''
    n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.

    **주의** : 소숫점 넷째자리에서 반올림하는 것은 고려할 필요가 없습니다. 이는 main()에서 출력을 할 때에 처리가 되므로, 기울기의 최댓값을 구하는 것에 집중해 주시길 바랍니다.
    '''
    
    result = -math.inf
    
    # loop 돌면서 모든 점 2쌍을 찾고 최대 기울기 갱신
    for idx1 in range(len(points)):
        for idx2 in range(idx1+1, len(points)):
            gradient = getGradient(points[idx1], points[idx2])
            
            result = max(result, gradient)
    
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % maxSlope(points))

if __name__ == "__main__":
    main()
