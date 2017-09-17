class Person:
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def __repr__(self):
    return 'Person: %s (%d cm)' % (self.name, self.height)

  def grow(self, factor):
    self.height = factor * self.height

  def taller_than(self, height):
    return self.height > height

p = Person('Fred', 150)
assert p.name == 'Fred'
assert p.height == 150
assert str(p) == 'Person: Fred (150 cm)'
assert p.taller_than(149)
p.grow(1.1)
assert p.height == 165
