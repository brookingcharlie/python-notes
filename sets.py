s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(3)

assert len(s) == 3

# checking set membership is very fast
# unlike lists, which have to check every element
assert 1 in s
assert 4 not in s
