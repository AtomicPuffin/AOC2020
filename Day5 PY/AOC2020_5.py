from typing import *

def translate(boarding_pass:str) -> Tuple[int,int]:
    result = ''
    for char in range(len(boarding_pass)):
        if boarding_pass[char] in ['F', 'L']:
            result += '0'
        elif boarding_pass[char] in ['B', 'R']:
            result += '1'
        else:
            raise ValueError('Unknown instruction')
    return result


# Find max seat ID
def part_one(boarding_passes: List[str]) -> int:
    return max(int(translate(i), 2) for i in boarding_passes)   

# Find empty seat
def part_two(boarding_passes: List[str]) -> int:
    ids = [int(translate(p),2) for p in boarding_passes]
    ids = sorted(ids)
    for i in ids:
        if i+1 not in ids:
            return i+1

def main() -> None:
    input = [x.rstrip() for x in (open('input.txt').readlines())]
    print('Answer to part 1: ',part_one(input))
    print('Answer to part 2: ',part_two(input))

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)