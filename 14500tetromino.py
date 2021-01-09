"""5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1"""
a = list(map(int, (input().split())))
b = int(a[0])*int(a[1])

map = [list(map(int, input().split())) for _ in range(a[0])]

map2 = []
for i in range(len(map)):
    for j in map[i]:
        map2.append(j)
map2.sort(reverse=True)
print(map2)

num = []
for i in range(1,len(map2)):
    if map2[i] !=map2[i-1]:
        num.append[map2[i]]
        calculate(map, num)
#
#
def search(map, num):
    
1일단 한 점을 찍고 그 점에서부터 나아근ㄴ 방향

2그냥 4개 모양맞춰서 찍고 합산

3큰 수부터 이어질 수 있는 알고리즘을 구현 (채택)


    
