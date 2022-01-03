def GCD(x, y) :
    '''
    x, y의 최대공약수를 반환하는 함수
    '''
    # base condition
    if y == 0:
        return x

    # recursive
    return GCD(y, x%y)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = input()

    x = int(data.split()[0])
    y = int(data.split()[1])

    print(GCD(x, y))

if __name__ == "__main__":
    main()


