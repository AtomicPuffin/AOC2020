from typing import *

# a-b c: abc
# Find passwords with c appearing a to b times in abc
def part_one(pwds: List[str]) -> int:
    counter = 0
    for i in pwds:
        word = i.split()
        min, max = int(word[0].split("-")[0]), int(word[0].split("-")[1])
        letter = word[1][0]
        pwd = word[2]
        if min <= pwd.count(letter) <= max:
            counter += 1
    return counter

# a-b c: abc
# Find passwords with c appearing in either position a or b in abc
def part_two(pwds: List[int]) -> int:
    counter = 0
    for i in pwds:
        word = i.split()
        min, max = int(word[0].split("-")[0]), int(word[0].split("-")[1])
        letter = word[1][0]
        pwd = word[2]
        if (
            letter in [pwd[min - 1], pwd[max - 1]]
            and pwd[min - 1] != pwd[max - 1]
        ):
            counter += 1
    return counter

def main() -> None:
    password_list = list(open('input.txt').readlines())
    print('Answer to part 1: ',part_one(password_list))
    print('Answer to part 2: ',part_two(password_list))

if __name__ == "__main__":
    try:
        main()
    except ValueError as ve:
        print(ve)
