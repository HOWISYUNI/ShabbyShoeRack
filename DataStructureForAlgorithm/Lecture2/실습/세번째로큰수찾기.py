import math

'''
정렬해서 세번째를 찾으면 O(NlogN)
단순히 첫번째, 두번째, 세번째 큰 수를 for문에서 계속 갱신하면 O(N)
N번째 큰수는 계속 기억하는게 정렬보다 빠르다
'''
def thirdMax(nums):
    
    first, second, third = -math.inf, -math.inf, -math.inf
    
    for num in nums:
        if num > first:
            first, second, third = num, first, second
        elif num > second:
            second, thrid = num, second
        elif num > third:
            third = num
            
    return third
    

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()
