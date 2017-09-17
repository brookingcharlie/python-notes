ns = [1, 2, 3]
vs = ['foo', True, ns]
trailing = [1, 2, ]

assert ns == [1, 2, 3], '== compares list elements'
assert sum(ns) == 6, 'python has a built-in sum method'
assert len(vs) == 3, 'python has a built-in length method'
assert trailing == [1, 2], 'list syntax allows a comma at the end'

assert 1 in ns, 'in expr tests element membership'
assert 5 not in ns, 'not-in expr denotes element non-membership'

a, b = [1, 2]
assert (a, b) == (1, 2), 'assignment can deconstruct lists'

# indexing/slicing

r = [0, 1, 2, 3, 4]

assert r[0] == 0, 'index 0 fetches first element'
assert r[4] == 4, 'index n fetches nth zero-based element'
assert r[-1] == 4, 'index -1 fetches last element'
assert r[-2] == 3, 'index -n fetches nth-last element'

assert r[1:3] == [1, 2], 'slicing n:m gives nth to (m-1)th elements'
assert r[:3] == [0, 1, 2], 'slicing :m gives 0th to (m-1)th elements'
assert r[3:] == [3, 4], 'slicing n: gives nth element onwards'
assert r[:] == [0, 1, 2, 3, 4], 'slicing : copies the list'

# concat/append

xs = [1, 2, 3]
assert xs + [4, 5, 6] == [1, 2, 3, 4, 5, 6], '+ concatenates two lists'
assert xs == [1, 2, 3], '+ does not modify the list'
assert xs.extend([4, 5, 6]) == None, 'extend appends all elements from given list'
assert xs == [1, 2, 3, 4, 5, 6], 'extends modifies the list'
assert xs.append(7) == None, 'append single element'
assert xs == [1, 2, 3, 4, 5, 6, 7], 'append modifies the list'

# sorting

ys = [4, 2, 1, 3]
assert sorted(ys) == [1, 2, 3, 4]
assert ys == [4, 2, 1, 3], 'sorted does not modify list'
assert ys.sort() == None
assert ys == [1, 2, 3, 4], 'sort does modify list'

# comprehensions

even_squares = [x * x for x in range(5) if x % 2 == 0]
coords = [(x, y) for x in range(2) for y in range(3)]
zeroes = [0 for _ in range(5)] # use _ as conventional name
assert even_squares == [0, 4, 16]
assert coords[0] == (0, 0)
assert coords[-1] == (1, 2)
assert len(zeroes) == 5
