import AOC2020_3

forest = list(open('input_test.txt').readlines())

def test_one():
    assert AOC2020_3.part_one(forest) == 7

def test_two():
    assert AOC2020_3.part_two(forest) == 336