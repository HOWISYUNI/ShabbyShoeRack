def getDigit(num):
    # num의 자릿수를 구하는 함수
    return len(str(num))

def diffDigit(a, b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''
    
    # 자릿수 구하기
    digitA = getDigit(a)
    digitB = getDigit(b)
    
    diff = abs(digitA - digitB)
    a = str(a)
    b = str(b)
    
    if diff != 0:
        # 작은 자리숫자에 0채우기
        if len(str(a)) < len(str(b)):
            a = '0'*diff + a
        else:
            b = '0'*diff + b
            
    # 두 숫자의 서로 다른 자리 숫자 비교
    result = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()
