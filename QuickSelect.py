def quick_selection(arr, k):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr)//2]    # pivot값 중앙값으로 설정
  A, B, C = [], [], []
  
  for i in range(len(arr)):
    if arr[i] < pivot:        # pivot값보다 작으면
      A.append(arr[i])        # A리스트에 추가
    elif arr[i] > pivot:      # pivot값보다 크면
      C.append(arr[i])        # C리스트에 추가      
    else: B.append(arr[i])
  
  if k < len(A):                  # k번째 작은 값이 A리스트의 원소 갯수보다 적으면
    return quick_selection(A, k)  # A리스트에 k번쨰로 작은 값이 존재하므로 재귀
  elif k > len(A) + len(B):
    return quick_selection(C, k - len(A) - len(B))
  else: return pivot

n, k = map(int, input().split())
L = list(map(int, input().split()))

print(quick_selection(L,k))
