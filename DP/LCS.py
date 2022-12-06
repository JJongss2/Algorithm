Pseudo code
def LCS(X, Y):
  n, m = |X|, |Y|
  # prepare 2d list len and initialization
  for j in range(0, m+1): len[0][j] = 0
  for i in range(0, n+1): len[i][0] = 0
    
  # filling DP table len
  for i in range(1, n+1):
    for j in range(1, m+1):
      if X[i] == Y[j]: # 마지막 두 글자가 같으면
        len[i][j] = len[i-1][j-1] + 1
      else: # 마지막 글자가 다르면
        len[i][j] = max(len[i-1][j], len[i][j-1])
  return len[n][m]
