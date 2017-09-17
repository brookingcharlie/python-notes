ns = [1, 2, 3]
vs = ['foo', 0.1, True]
ls = [ns, vs, []]

assert ns == [1, 2, 3], '== compares list elements'
assert sum(ns) == 6, 'python has a built-in sum method'
assert len(ls) == 3, 'python has a built-in length method'
assert [1, 2, ] == [1, 2], 'list syntax allows a comma at the end'

r = [0, 1, 2, 3, 4]

assert r[0] == 0, 'index 0 fetches first element'
assert r[4] == 4, 'index n fetches nth zero-based element'
assert r[-1] == 4, 'index -1 fetches last element'
assert r[-2] == 3, 'index -n fetches nth-last element'

assert r[1:3] == [1, 2], 'slicing n:m gives nth to (m-1)th elements'
assert r[:3] == [0, 1, 2], 'slicing :m gives 0th to (m-1)th elements'
assert r[3:] == [3, 4], 'slicing n: gives nth element onwards'
assert r[:] == [0, 1, 2, 3, 4], 'slicing : copies the list'

assert 1 in r, 'in expr tests element membership'
assert 5 not in r, 'not-in expr denotes element non-membership'

xs = [1, 2, 3]

assert xs + [4, 5, 6] == [1, 2, 3, 4, 5, 6], '+ concatenates two lists'
assert xs == [1, 2, 3], '+ does not modify the list'
assert xs.extend([4, 5, 6]) == None, 'extend appends all elements from given list'
assert xs == [1, 2, 3, 4, 5, 6], 'extends modifies the list'
assert xs.append(7) == None, 'append single element'
assert xs == [1, 2, 3, 4, 5, 6, 7], 'append modifies the list'

a, b = [1, 2]
assert (a, b) == (1, 2), 'assignment can deconstruct lists'
