from typing import *
import re

''' Rules
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''
#Test if passport field is valid
def test_field(field: str) -> bool:
    if field.startswith('byr'):
        return 1920 <= int(field.split(':')[1]) <= 2002
    elif field.startswith('iyr'):
        return 2010 <= int(field.split(':')[1]) <= 2020
    elif field.startswith('eyr'):
        return 2020 <= int(field.split(':')[1]) <= 2030
    elif field.startswith('hgt'):
        if field[-2:] == 'cm':
            return 150 <= int(field.split(':')[1][:-2]) <= 193          
        elif field[-2:] == 'in':
            return 59 <= int(field.split(':')[1][:-2]) <= 76
        else:
            return False
    elif field.startswith('hcl'):
        return bool(re.search(r'^#[0-9a-f]{6}', field.split(':')[1]))
    elif field.startswith('ecl'):
        return field.split(':')[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field.startswith('pid'):
        return bool(re.search(r'\b\d{9}\b', field.split(':')[1]))
    elif field.startswith('cid'):
        return True
    else:
        raise ValueError ('Unknown field')

#Test if passport is valid
def test_passport(passport: List[str]) -> bool:
    required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    temp = [y[:3] for y in passport]
    return all((i in temp) for i in required)

# Find passports with all 7 required fields present
def part_one(passports: List[List[str]]) -> int:
    return sum(1 for i in passports if test_passport(i))

# Find passports with all seven fields valid
def part_two(passports: List[List[str]]) -> int:
    return sum(
        bool(
            test_passport(passport)
            and all(test_field(field) for field in passport)
        )
        for passport in passports
    )

def main() -> None:
    input = [i.split() for i in (open('input.txt').read().split('\n\n'))]
    print('Answer to part 1: ',part_one(input))
    print('Answer to part 2: ',part_two(input))

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)