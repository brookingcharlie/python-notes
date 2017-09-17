s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(3)

assert len(s) == 3

# checking set membership is fast (unlike lists, which have to check every element)

assert 1 in s
assert 4 not in s

# comprehensions

squares = {x * x for x in range(5)}
assert squares == {0, 1, 4, 9, 16}
