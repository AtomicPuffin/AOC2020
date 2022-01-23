import AOC2020_3
import os

def test_one():
    mydir = os.path.dirname(__file__) + '/example.txt'
    forest = list(open(mydir).readlines())
    assert AOC2020_3.part_one(forest) == 7

def test_two():
    mydir = os.path.dirname(__file__) + '/example.txt'
    forest = list(open(mydir).readlines())
    assert AOC2020_3.part_two(forest) == 336