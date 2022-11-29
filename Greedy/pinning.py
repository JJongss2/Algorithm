n = int(input())
arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append([a, b])
arr.sort(key = lambda x : x[1]) # 두번째 원소를 기준으로 오름차순 정렬
L, selected = [0], 0
for i in range(1, n):
  if arr[selected][1] < arr[i][0]:
    L.append(i)
    selected = i
print(len(L))
