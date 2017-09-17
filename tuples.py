coords = (1, 2, 3)
assert coords[0] == 1, 'index 0 fetches first element'
assert coords[2] == 3, 'index n fetches nth zero-based element'

s, p = (3, 2)
assert (s, p) == (3, 2), 'assignment by deconstructing tuple'

try:
  coords[1] = 3
  assert False, 'cannot modify a tuple'
except:
  pass

def sum_and_product(x, y):
  return (x + y), (x * y)

assert sum_and_product(1, 2) == (3, 2), 'tuple returned by function'

x, y = 1, 2
x, y = y, x
assert (x, y) == (2, 1), 'pythonic way to swap variables'
