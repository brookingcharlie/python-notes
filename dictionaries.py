assert dict() == {}, 'alternative ways to construct dictionaries'

grades = {'Joel': 80, 'Elle': 95}
grades['Tim'] = 75
assert grades['Joel'] == 80
assert grades['Elle'] == 95
assert grades['Tim'] == 75

try:
  grades['Foo']
  assert False, 'indexing on unknown key raises error'
except KeyError:
  pass

assert grades.get('Joel') == 80, 'get method is an alternative to indexing'
assert grades.get('Kate') == None, 'get returns None as deault instead of raising KeyError'
assert grades.get('Kate', 0) == 0, 'get can return a given default value instead'

assert len(grades) == 3
assert sorted(grades.keys()) == sorted(['Joel', 'Elle', 'Tim'])
assert sorted(grades.values()) == sorted([80, 95, 75])

assert 'Joel' in grades
assert 'Kate' not in grades
assert ('Elle' in grades) == ('Elle' in grades.keys()), 'in expr checks key membership'

# defaultdict

from collections import defaultdict

word_counts = defaultdict(int)
word_counts['the'] = 1024
assert word_counts['the'] == 1024
assert word_counts['foo'] == 0, 'calls int() to create default value 0'

offspring = defaultdict(list)
assert offspring['foo'] == [], 'calls list() to default to an empty list'

discount = defaultdict(lambda: 0.50)
assert discount['oranges'] == 0.5, 'calls given default_factory function'

# counters

from collections import Counter

c = Counter([0, 1, 2, 0, 2, 3, 4, 2])
assert c[2] == 3
assert c[5] == 0
assert c.most_common(3) == [(2, 3), (0, 2), (1, 1)], 'n most common elements and their counts'
