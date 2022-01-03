import math

def howManyTree(n, myInput) :
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''
    
    # 간격
    gangyuk = list(set([abs(myInput[i] - myInput[i+1]) for i in range(len(myInput)-1)]))

    # 간격들 최대공약수 중 가장 큰 것
    gcdMax = 1
    for i in range(len(gangyuk)-1):
        tempGCD = GCD(gangyuk[i], gangyuk[i+1])
        if gcdMax < tempGCD:
            gcdMax = tempGCD

    # 더 심어야 하는 위치에 심어서 cnt 늘리기
    cnt = 0
    treeLimitation = max(myInput)
    now = min(myInput)

    while now < treeLimitation:
        nextPos = now + gcdMax
        if nextPos == treeLimitation:
            break
        elif nextPos in myInput:
            now = nextPos
            continue

        now = nextPos
        cnt += 1

    return cnt


def GCD(A, B):
    
    # base condition
    if B == 0:
        return A

    # recursive
    return GCD(B, A%B)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    print("문제 설명의 입력 예시를 모두 복사한 후, 한번에 붙여넣어 주세요")
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print("같은 간격이 되도록 새로 심어야 하는 가로수의 최소 수는 {}개 입니다.".format(howManyTree(n, myInput)))
if __name__ == "__main__":
    main()
