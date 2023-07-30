from test import *

def test_add():
  assert add(3,5) == 8

def test_subtract():
  assert sub(4,2) == 2

def test_mul():
  assert mul(2,3) == 6

def test_div():
  assert div(3,1) == 3
  assert div(3,4) == 2
  assert div(3,0) == 0
