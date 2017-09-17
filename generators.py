# defining a generator

def lazy_range(n):
  i = 0
  while i < n:
    yield i
    i += 1

# iterating over a generator

xs = []
for x in lazy_range(5):
  xs.append(x)
assert xs == [0, 1, 2, 3, 4]

# manually fetching values

r1 = lazy_range(2)
assert r1.next() == 0
assert r1.next() == 1
try:
  r1.next()
  assert False, 'should not yield any more'
except StopIteration:
  pass

# constructing lists from generators

r2 = lazy_range(3)
assert list(r2) == [0, 1, 2], 'construct list with fresh generator'
assert list(r2) == [], 'trying again yeilds no elements (does not raise exception)'

# comprehensions

lazy_evens = (i for i in lazy_range(10) if i % 2 == 0)
assert [lazy_evens.next(), lazy_evens.next()] == [0, 2]
