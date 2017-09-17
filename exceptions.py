try:
  print 0 / 0
  assert False, 'exception should have been thrown'
except ZeroDivisionError:
  pass
