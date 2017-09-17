assert dict() == {}, 'alternative ways to construct dictionaries'

grades = {'Joel': 80, 'Tim': 95}
assert grades['Joel'] == 80
assert grades['Tim'] == 95

try:
  grades['Foo']
  assert False, 'indexing on unknown key raises error'
except KeyError:
  pass
