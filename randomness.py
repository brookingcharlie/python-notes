import random

# generating a random number

r = random.random()
assert r >= 0.0 and r < 1.0, 'random number in mathematical range [0.0,1.0)'

# seeding the random number generator

random.seed(10); r1 = random.random()
random.seed(10); r2 = random.random()
assert r1 == r2, 'given same seed, pseudorandom numbers are reproducible'

# random choice from a python range

random.seed()
rr1 = random.randrange(10)
rr2 = random.randrange(3, 6)
assert rr1 >= 0 and rr1 < 10, 'random element from range(10)'
assert rr2 >= 3 and rr2 < 6, 'random element from range(3, 6)'

# randomly choosing elements

random.seed()
people = ['Alice', 'Bob', 'Charlie']
rc = random.choice(people)
assert rc in people

# shuffling a list

random.seed()
numbers = [0, 1, 2]
rs = random.shuffle(numbers)
assert sorted(numbers) == [0, 1, 2]

# randomly sampling elements without duplicates

random.seed()
unique_choices = random.sample(range(60), 6)
assert all(x in range(60) for x in unique_choices)
assert len(unique_choices) == 6
assert len(set(unique_choices)) == 6, 'contains no duplicates'

# randomly sampling elements allowing duplicates

random.seed()
non_unique_choices = [random.choice(range(10)) for _ in range(5)]
assert all(x in range(10) for x in non_unique_choices)
assert len(non_unique_choices) == 5
assert len(set(non_unique_choices)) <= 5, 'contains no duplicates'
