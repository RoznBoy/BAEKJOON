import sys
input = sys.stdin.readline

N = int(input())

### 첫번째 풀이 : 틀림 -> 어쩐지 너무 간단하다 싶더니
'''
distance = 0
person = 0
for _ in range(N):
    X, A = map(int, input().split())
    person += A
    distance += X*A
    
print(distance//person)
'''
### 두번째 풀이 : 너무 단순하게 생각해서 고려 안한 것들이 많음 -> 최단 거리가 여러개가 나올 수 있음
'''
진짜 도저히 뭔지 몰라서 검색
문제 접근 방법은 누적 인구 수가 총 인구 수의 절반을 넘어가는 지점을 찾는 것 -> 직관 적으로 이해 안됨;; 사람이 많아도 거리 차이가 크면 무시할 수 있지않나? 
일단 고려해야 할 사항은 마을 번호를 순서대로 알려주는게 아니다 -> 정렬 필요
카마니 생각해보면 마을 번호는 거리에 중요하지 않네!! 번호 상관 없이 수직선 칸 이동한다고 생각하면 사람 수 누적만 따지면 돼
'''
