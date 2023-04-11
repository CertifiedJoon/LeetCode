def matrix01(mat):
  m, n = len(mat), len(mat[0])
  for r in range(m):
    for c in range(n):
      if mat[r][c] == 0:
        continue
      if r > 0:
        mat[r][c] = min(mat[r][c], mat[r-1][c] + 1)
      if c > 0:
        mat[r][c] = min(mat[r][c], mat[r][c-1])
  
  for r in range(m - 1, -1, -1):
    for c in range(n - 1, -1, -1):
      if mat[r][c] == 0:
        continue
      if r + 1 < m:
        mat[r][c] = min(mat[r][c], mat[r+1][c] + 1)
      if c + 1 < n:
        mat[r][c] = min(mat[r][c], mat[r][c+1])