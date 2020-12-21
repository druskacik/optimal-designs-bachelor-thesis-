def create_optimal_matrix(n):
  matrix = []
  if n % 2 == 0:
    for i in range(n):
      row = [0 for j in range(n)]
      for j in range(n//2):
        if i < n/2:
          row[j] = 1
        else:
          row[n - j - 1] = 1
      matrix.append(row)
  else:
    for i in range(n):
      row = [0 for j in range(n)]
      if i < n//2:
        for j in range(n//2):
          row[j] = 1
      else:
        for j in range(n//2 + 1):
          row[n - j - 1] = 1
        row[i] = 0
      matrix.append(row)
  return matrix

def identity(n):
  matrix = []
  for i in range(n):
    row = [0 for j in range(n)]
    row[i] = 1
    matrix.append(row)
  return matrix