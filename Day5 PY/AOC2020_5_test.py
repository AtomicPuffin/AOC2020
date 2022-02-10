import AOC2020_5
import os

def test_translate():
    assert AOC2020_5.translate('FBFBBFFRLR') == '0101100101'
    
def test_one():
    assert AOC2020_5.part_one(['FBFBBFFRLR']) == 357

def test_two():
    mydir = os.path.dirname(__file__) + '/input.txt'
    input = [x.rstrip() for x in (open(mydir).readlines())]
    assert AOC2020_5.part_two(input) == 504