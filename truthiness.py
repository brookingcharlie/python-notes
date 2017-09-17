# boolean literals

assert True, 'boolean true literal'
assert not False, 'boolean false literal'

# Python uses None to denote a nonexistent value

x = None
assert x == None
assert x is None

# falsy values

assert not False
assert not None
assert not []
assert not {}
assert not ''
assert not set()
assert not 0
assert not 0.0

# truthy values

assert True
assert [1]
assert {'a': 1}
assert 'a'
assert set([1])
assert 1
assert 0.1

# all/any stmts

assert all([True, [1], {'a': 1}])
assert any([False, None, 1])
assert all([]), 'since no falsy element in list'
assert not any([]), 'since no truthy elements in list'
