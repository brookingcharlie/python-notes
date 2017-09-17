from functools import partial

# currying

def exp(base, power): return base ** power
two_to_the = partial(exp, 2)
square_of = partial(exp, power=2)

assert two_to_the(3) == 8, 'uses default for base'
assert square_of(3) == 9, 'uses defalt for power'

# map/reduce/filter

xs = [1, 2, 3, 4]
def twice(n): return 2 * n
def even(n): return n % 2 == 0
def product(n, m): return n * m
twice_mapper = partial(map, twice)
even_filterer = partial(filter, even)
product_reducer = partial(reduce, product)

assert map(twice, xs) == [2, 4, 6, 8]
assert twice_mapper(xs) == [2, 4, 6, 8]
assert [twice(x) for x in xs] == [2, 4, 6, 8], 'comprehension notation'

assert filter(even, xs) == [2, 4]
assert even_filterer(xs) == [2, 4]
assert [x for x in xs if even(x)] == [2, 4], 'comprehension notation'

assert reduce(product, xs) == 24
assert product_reducer(xs) == 24
