import re

IN_FILE_PATH = "advent_of_code/2024/day3/3.txt"


def parse_lines(infile: str) -> list[dict]:
    with open(infile, "r") as file:
        return [line for line in file]


def day_3a(infile):

    lines = parse_lines(infile)
    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    result = 0
    for l in lines:
        matches = re.findall(pattern, l)
        for m in matches:
            result += int(m[0]) * int(m[1])

    return result


print(day_3a(IN_FILE_PATH))
# print(day_2b(IN_FILE_PATH))
assert day_3a(IN_FILE_PATH) == 169021493
# assert day_2b(IN_FILE_PATH) == 71585
