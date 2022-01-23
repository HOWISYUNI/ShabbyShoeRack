'''
두 개의 문자열이 주어집니다. 이때 두번째 문자열은 첫번째 문자열에 하나의 문자를 추가한 후, 그 순서를 랜덤하게 뒤섞은 문자입니다. 이때 추가된 문자를 찾아보도록 합시다.

예를 들어서, apple 과 azlppe 가 주어졌을 경우 추가된 문자는 z입니다.

추가된 문자는 하나라고 가정해도 좋습니다.
추가된 문자가 이미 리스트에 존재하던 문자 일 수도 있습니다.
'''

def findDifference(str1, str2):
    dict1 = dict()
    dict2 = dict()
    
    for char1 in str1:
        dict1[char1] = dict1.get(char1, 0) + 1
        
    for char2 in str2:
        dict2[char2] = dict2.get(char2, 0) + 1
        
    for key2 in dict2.keys():
        if key2 not in dict1.keys() or dict1[key2] != dict2[key2]:
            return key2

def main():
    print(findDifference("apple", "aalppe"))
    

if __name__ == "__main__":
    main()
