from project_math.matrices import compute_all_binary_matrices
from project_math.variance import compute_variance

def compute_singular_designs(m, n):
  singular_designs = []
  binary_matrices = compute_all_binary_matrices(m, n)
  for matrix in binary_matrices:
    variance = compute_variance(matrix)
    if variance == float('inf'):
      singular_designs.append(matrix)
  return singular_designs

def save_singular_designs(m, n):
  singular_designs = compute_singular_designs(m, n)
  text_file = open('data/singular_designs/designs' + str(m) + 'x' + str(n) + '.txt', 'w')
  for index, design in enumerate(singular_designs):
      text_file.write('Design ' + str(index + 1) + '\n')
      for row in design:
          text_row = ''
          for i in row:
              text_row += str(i) + ' '
          text_file.write(text_row + '\n')
      text_file.write('\n')
  text_file.close()
  print('Successfully computed and saved desings ' + str(m) + ' x ' + str(n))

# usage:
# save_singular_designs(2, 2)

print('END')