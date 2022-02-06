'''
문자열 압축(2020 KAKAO 신입공채)

풀이시간 : 30분
시간제한 : 1초
메모리제한 : 128MB

주어진 문자열 S를 n개 단위로 잘라서 압축한다
최대로 압축한 문자열의 길이를 리턴한다.

[SOLUTION 1]
n단위로 자른 두 덩어리(1, 2 문자열)를 비교해야한다
n단위는 1 ~ len(s)//2 임, mid가 s 길이의 절반을 넘어가면 unit의 의미가 없음
start --(1)-- mid --(2)-- end

for unit크기:
    while mid <= len(s): -> mid가 s 길이의 절반을 넘어가면 unit의 의미가 없음
        if 1 == 2
            cnt(동일 문자열 수 기억)

        elif 1 != 2
            compress -> cnt+(1)을 압축된 문자열에 추가
            if end > len(s) : 
                compress -> mid 기준으로 while문을 돌리므로 len(s)를 넘어간 end 조각처리를 해줘야함
            

[SOLUTION 2] # UNIT 단위로 일단 S를 잘라놓고 ZIP을 통해 좌 우를 비교해 압축

* 배울 점
1. [i : i + unitSize] 면  i에서 유닛사이즈만큼 잘 잘라주니 걱정하지 않아도된다
2. idx 단위로 두 덩어리를 비교할 때 일단 잘라놓고 zip을 활용하면 편하다
    zip은 두 리스트 원소 짧은거에 맞추니까 완전하게 맞추고 싶으면 짧은거에 원소 하나를 더 더해야한다
3. 리스트 + 연산과 append : 
    1. 리스트 + 연산 : 원소가 더해진 리스트 리턴
    2. 리스트.append(원소) : None을 리턴. 다시 리스트 객체로 처리해야한다.

'''

# [SOLUTION 1]
# def solution(s):
#     maxCompressed = s

#     # unit : 1 ~ len(s)//2
#     for unitSize in range(1, (len(s))//2+1):
#         # 초기화
#         start, mid, end = 0, unitSize, unitSize*2
#         compressed = ''
#         cnt = 1

#         # 현재 unitsize로 compress
#         while mid <= len(s):
#             str1 = s[start:mid]
#             str2 = s[mid:end]

#             if str1 == str2:
#                 cnt += 1
            
#             else: # str1 != str2
#                 compressed = updateCompressed(str1, compressed, cnt)
#                 cnt = 1
#                 if end > len(s): # 마지막 부분 조각 처리
#                     compressed = updateCompressed(str2, compressed, cnt)
#                     break

#             # s, m, e 갱신
#             start = start + unitSize
#             mid = mid + unitSize
#             end = end + unitSize

#         print("unit size : " + str(unitSize) + " / compressed : " + compressed)

#         # 최대 압축 갱신
#         if len(compressed) < len(maxCompressed):
#             maxCompressed = compressed


#     return len(maxCompressed)


# [SOLUTION 2]
def solution(s):

    def compress(string, cnt):
        return string if cnt == 1 else str(cnt)+string

    maxCompressed = s

    for unitSize in range(1, (len(s)//2)+1):
        words = [s[i:i+unitSize] for i in range(0, len(s), unitSize)]
        # print('---- unit size : ' + str(unitSize))
        # print(words)
        cnt = 1
        compressed = ''
        for strA, strB in zip(words, words[1:]+['']):
            if strA == strB:
                cnt += 1
            else:
                compressed += compress(strA, cnt)
                cnt = 1

        maxCompressed = compressed if len(compressed) < len(maxCompressed) else maxCompressed
        # print('unit sieze : ' + str(unitSize) + " / max compressed : " + maxCompressed)

    return len(maxCompressed)


def updateCompressed(string, compressed, cnt):
    if cnt == 1:
        compressed = compressed+string
    else:
        compressed = compressed+(str(cnt)+string)

    return compressed

if __name__ == "__main__":
    # s = 'aabbaccc'
    # s = 'ababcdcdababcdcd'
    s = 'abcabcdede'
    # s = 'abcabcabcabcdededededede'
    # s = 'xababcdcdababcdcd'

    print(solution(s))