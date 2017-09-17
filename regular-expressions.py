import re

assert not re.match('a', 'cat'), "'cat' doesn't start with an 'a'"
assert re.search('a', 'cat'), "'cat' contains an 'a'"
assert not re.search('c', 'dog'), "'dog' doesn't contain an 'a'"
assert re.split('[ab]', 'carbs') == ['c', 'r', 's']
assert re.sub('[0-9]', '-', 'R2D2') == 'R-D-'
