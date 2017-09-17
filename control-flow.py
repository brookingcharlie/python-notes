# if stmts

if 1 > 2:
  assert False, 'nope'
elif 1 > 3:
  assert False, 'try again'
else:
  pass

# ternary exprs

def parity(x): return 'even' if x % 2 == 0 else 'odd'
assert parity(4) == 'even'
assert parity(3) == 'odd'

# while loops

x = 0
while x < 10:
  x += 1
assert x == 10

# for loops

count = 0
for i in range(10):
  if i == 3:
    continue
  if i == 5:
    break
  count += 1
assert count == 4
