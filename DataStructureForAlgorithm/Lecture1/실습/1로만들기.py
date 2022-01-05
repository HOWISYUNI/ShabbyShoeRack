# divide and conquer를 이용한 풀이

import math

def convertTo1(num):
    div2result, div3result, minusResult = math.inf, math.inf, math.inf
    
    # base condition
    if num == 1:
        return 0
    
    # conquer
    if num%2 == 0:
        div2result = convertTo1(num//2)
    if num%3 == 0:
        div3result = convertTo1(num//3)
    else:
        minusResult = convertTo1(num-1)
        
    return min(div2result+1, div3result+1, minusResult+1)

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
