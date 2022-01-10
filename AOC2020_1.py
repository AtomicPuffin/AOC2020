from typing import *

# Find first pair in input that sums to 2020
def part_one(report: List[int]) -> int:
    for _ in report:
        row = 2020 - report.pop(0)
        for i in report:
            if row == i:
                return i * (2020 - i)
    raise ValueError('Input ended with no match')

# Find first triplet in input that sums to 2020
def part_two(report: List[int]) -> int:
    for _ in report:
        bc = 2020 - report.pop(0)
        r_temp = report.copy()
        for _ in r_temp:
            c = bc - r_temp.pop(0)
            for i in r_temp:
                if c == i:
                    return c * (bc - c) * (2020 - bc)
    raise ValueError('Input ended with no match')
    
def main() -> None:
    expense_report = [int(i) for i in open('input1.txt').readlines()]
    print(part_one(expense_report.copy()))
    print(part_two(expense_report.copy()))

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
