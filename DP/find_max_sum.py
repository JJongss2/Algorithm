n = int(input())
arr = list(map(int, input().split()))
def find_max_sum(arr):
  s = [0] * len(arr)
  s[0] = arr[0]
  for i in range(1, n):
    s[i] = max(s[i-1] + arr[i], arr[i])
  return max(s)

print(find_max_sum(arr))
