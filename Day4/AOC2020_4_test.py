import AOC2020_4
import os

def test_test_field():
    test = 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'
    for i in test.split():
        assert AOC2020_4.test_field(i) == True

def test_test_passport():
    test = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'.split()
    assert AOC2020_4.test_passport(test) == True
    
def test_one():
    mydir = os.path.dirname(__file__) + '/example.txt'
    input = [i.split() for i in (open(mydir).read().split(2*os.linesep))]
    assert AOC2020_4.part_one(input) == 8

def test_two():
    mydir = os.path.dirname(__file__) + '/example.txt'
    input = [i.split() for i in (open(mydir).read().split(2*os.linesep))]
    assert AOC2020_4.part_two(input) == 4