from typing import *

# Count trees (#) on slope x,y
def slope(forest: List[str], x: int, y: int) -> int:
    counter = 0
    position = 0
    slice = len(forest[0])-1
    depth = 0
    while depth < len(forest):
        if forest[depth][position] == "#":
            counter += 1
        if position + x < slice:
            position += x
        else:
            position = ((position+x) % slice)
        depth += y
    return counter

# Find trees on slope 3:1
def part_one(forest: List[str]) -> int:
    return slope(forest, 3, 1)

# Find trees on slopes 1:1, 3:1, 5:1, 7:1, 1:2
def part_two(forest: List[int]) -> int:
    return (slope(forest, 1, 1) 
            * slope(forest, 3, 1) 
            * slope(forest, 5, 1)
            * slope(forest, 7, 1) 
            * slope(forest, 1, 2)
            )

def main() -> None:
    forest = list(open('input.txt').readlines())
    print('Answer to part 1: ',part_one(forest))
    print('Answer to part 2: ',part_two(forest))

if __name__ == "__main__":
    main()