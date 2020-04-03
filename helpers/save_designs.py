def save_designs(path, designs):
  m, n = 0, 0
  if len(designs) > 0:
      m, n = designs[0].shape
  else:
      return
  text_file = open(path + '/designs' + str(m) + 'x' + str(n) + '.txt', 'w')
  for index, design in enumerate(designs):
      text_file.write('Design ' + str(index + 1) + '\n')
      for row in design:
          text_row = ''
          for i in row:
              text_row += str(i) + ' '
          text_file.write(text_row + '\n')
      text_file.write('\n')
  text_file.close()