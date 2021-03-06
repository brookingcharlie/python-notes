def sq(n):
  return n * n

sq_v2 = lambda n: n * n

assert sq(2) == 4, 'calling def-defined function'
assert sq_v2(2) == 4, 'calling lambda-defined function'

# higher-order functions

def apply(f, n): return f(n)

assert apply(sq, 2), 'passing a function argument by identifier'
assert apply(lambda n: n * n, 2), 'passing a function argument as a lambda'

# default args

def pow(n=2, m=3): return n ** m

assert pow() == 8, 'passing no arguments to function with default values'
assert pow(2) == 8, 'passing only first argument, using default for second'
assert pow(2, 3) == 8, 'passing both arguments, overriding their defaults'
assert pow(n=2, m=3) == 8, 'passing both arguments by name'
assert pow(m=3, n=2) == 8, 'passing both arguments by name in different order'
assert pow(n=1) == 1, 'passing only first argument by name, using defult for second'
assert pow(m=2) == 4, 'passing only second argument by name, using defult for first'

# argument unpacking

def add(a, b): return a + b
assert add(1, 2) == 3
assert add(*[1, 2]) == 3

# args and kwargs

def magic(*args, **kwargs):
  return \
    ['%d: %s' % (i, a) for i, a in enumerate(args)] + \
    ['%s: %s' % (i, k) for i, k in sorted(kwargs.items())]

assert magic(1, 2, x=5, y=7) == ['0: 1', '1: 2', 'x: 5', 'y: 7']

args = [12, 34]
kwargs = {'a': 1, 'b': 2}
assert magic(*args, **kwargs) == ['0: 12', '1: 34', 'a: 1', 'b: 2']
