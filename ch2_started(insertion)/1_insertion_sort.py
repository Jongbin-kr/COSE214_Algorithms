## 함수 정의
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]  ## i는 기준값을 가리키는 인덱스
        j = i - 1      ## j는 비교값을 가리키는 인덱스
        
        while j > -1 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        
        list[j+1] = key


## input값 처리
n = int(input())

l = []
for i in range(n):
    l.append(int(input()))


## 정렬 및 출력
insertion_sort(l)

for x in l:
    print(x)