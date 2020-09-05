import csv

def count_codes(fname, code_col):
  codes = set()

  with open(fname + '.csv', newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        codes.add(row[code_col])

  print(fname + ':')
  # Subtract one to eliminate header row
  print(len(codes) - 1)

fnames = ['observations', 'conditions', 'medications', 'procedures', 'allergies', 'careplans']
cols = [3, 4, 5, 3, 4, 5]
for i, fname in enumerate(fnames):
  count_codes(fname, cols[i])
