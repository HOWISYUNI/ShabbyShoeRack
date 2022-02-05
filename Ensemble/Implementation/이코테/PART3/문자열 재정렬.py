'''
풀이시간 : 20분
시간제한 : 1초
메모리제한 : 128MB

입력 문자열 -> 영문자열 오름차순 + 모든 숫자 합
1. 문자열 순회 -> 영문자, 숫자 분리
2. 영문자 오름차순 정렬
3. 숫자 합 
4. 결과값 출력

* 배울 내용
1. ord() 함수 : 문자 -> 유니코드 값
2. 리스트 -> 문자열 : {연결문자}.join(리스트)
'''

# inputVal = input()

# inputVal = 'K1KA5CB7'
inputVal = 'AJKDLSI412K4JSJ9D'

aAscii = ord('A')
numSum = 0
chars = []

for char in inputVal:
    if ord(char) < aAscii: # 숫자
        numSum += int(char)
    else: # 문자
        chars.append(char)

chars.sort()

print(''.join(chars)+str(numSum))