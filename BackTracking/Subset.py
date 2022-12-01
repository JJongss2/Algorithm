# 1
# S는 입력받은 합, A는 리스트, x는 뽑았는지 안뽑았는지 확인
def Backtrack1(k):
  current_sum = sum(A[i]*x[i] for i in range(k))
  if k == n: # 바닥조건
    if current_sum == S : print(x)
  else : # x[k] =1
    if current_sum + A[k] <= S:
      x[k]=1
      Backtrack1(k+1)
    x[k]=0 # 돌아오면 0으로 다시 설정
    Backtrack1(k+1)


    
    
    
def Backtrack2(k): # A의 값이 정렬되어 있음
  current_sum = sum(A[i]*x[i] for i in range(k))
  if k == n: return
  else:
    if current_sum + A[k] <= S:
      x[k] = 1 # 뽑음
      if current_sum + A[k] == S:
        print(x)
      else:
        Backtrack2(k+1)
      x[k]=0 # 안뽑음
      Backtrack2(k+1)
