from typing import *

# Find first pair in input that sums to total
def part_one(report: List[int], total: int) -> int:
    for _ in report:
        row = total - report.pop(0)
        for i in report:
            if row == i:
                return i * (total - i)
    raise ValueError('Input ended with no match')

# Find first triplet in input that sums to total
def part_two(report: List[int], total: int) -> int:
    for _ in report:
        bc = total - report.pop(0)
        r_temp = report.copy()
        for _ in r_temp:
            c = bc - r_temp.pop(0)
            for i in r_temp:
                if c == i:
                    return c * (bc - c) * (total - bc)
    raise ValueError('Input ended with no match')
    
def main() -> None:
    expense_report = [int(i) for i in open('input.txt').readlines()]
    print('Answer to part 1: ', part_one(expense_report.copy(), 2020))
    print('Answer to part 2: ', part_two(expense_report.copy(), 2020))

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
