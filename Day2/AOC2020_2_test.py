import AOC2020_2

def test_one():
    assert AOC2020_2.part_one(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 2

def test_two():
    assert AOC2020_2.part_two(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 1