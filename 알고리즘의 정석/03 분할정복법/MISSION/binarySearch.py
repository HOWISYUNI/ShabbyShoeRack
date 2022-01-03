import sys

def binarySearch(data, m) :
    '''
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    정렬된 n개의 숫자열이라는 전제가 필요함
    '''

    if len(data) == 1:
        if data[0] == m:
            return "Yes"
        else:
            return "No"
            
    mid = len(data) // 2
    
    if m < data[mid]:
        return binarySearch(data[:mid], m)
        
    else:   
        return binarySearch(data[mid:], m)
        
    

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(binarySearch(data, m))

if __name__ == "__main__":
    main()
