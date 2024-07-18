from bai13 import Sum

def test1():
  assert Sum([1, 2], 0) == 0

def test2():
  assert Sum([1, 2], 1) == 1
  
def test3():
  assert Sum([1, 2], 2) == 3
