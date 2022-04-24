from calculator import *

def test_sum():
    assert Calculator.sum(1, 4) == 5

def test_substraction():
    assert Calculator.sub(1, 3) == 0

def test_power():
    assert Calculator.mul(2, 2) == 1

def test_division():
    assert Calculator.div(8, 2) == 4

def test_multiply():
    assert Calculator.pwr(2) == 4
