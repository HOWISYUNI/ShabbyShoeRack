'''
정수 N이 입력되면 
00시 00분 00초 ~ N시 59분 59초 사이의 모든 시각 중 
3이 하나라도 포함되는 모든 경우의 수를 세자

시간제한 2초
메모리제한 128MB

[solution]
시각의 모든 경우의 수가 86400(24*60*60) 가지 이므로 3중 for문의 O(N) 알고리즘으로 해결할 수 있다
python 3.7은 2000만번 연산에 1초가 걸리기 때문이다.
'''

def solution(N):
    cnt = 0

    for hour in range(N+1):
        for minute in range(60):
            for sec in range(60):
                if isHaveThree(hour) or isHaveThree(minute) or isHaveThree(sec):
                    cnt += 1

    return cnt


def isHaveThree(time):
    return '3' in str(time)

if __name__ == "__main__":
    # N = int(input())
    N = 5
    print(solution(N))