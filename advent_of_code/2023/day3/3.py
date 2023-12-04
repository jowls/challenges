from collections import defaultdict
from math import prod

IN_FILE_PATH = "advent_of_code/2023/day3/3.txt"
IN_FILE_EX3 = "advent_of_code/2023/day3/ex_3.txt"


def parse_schematic(infile: str) -> list[list]:
    """Parse schematic from file

    Args:
        infile: Input file path

    Returns:
        2D matrix holding the engine schematic
    """

    with open(infile, "r") as file:
        return [[c for c in line.strip()] for line in file]


def day_3a(infile):
    sch = parse_schematic(infile)
    m = len(sch)  # of rows
    n = len(sch[0])  # of cols

    def special_search(i, j):
        # Searches for special characters surrounding the given location

        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if not (k == i and l == j) and 0 <= k < m and 0 <= l < n:
                    cur = sch[k][l]
                    if not cur.isnumeric() and cur != ".":
                        return True
        return False

    ans = 0
    for i, row in enumerate(sch):
        nums = []
        part_num = False
        for j, col in enumerate(sch[i]):
            cur = sch[i][j]
            if cur.isnumeric():
                nums.append(sch[i][j])
                if not part_num:
                    part_num = special_search(i, j)
            else:
                if part_num:
                    ans += int("".join(nums))
                nums.clear()
                part_num = False
        if part_num and nums:
            ans += int("".join(nums))

    return ans


def day_3b(infile):
    sch = parse_schematic(infile)
    m = len(sch)  # of rows
    n = len(sch[0])  # of cols
    stars = defaultdict(list)

    def star_search(i, j):
        # Searches for "*" chars surrounding given location and returns their location

        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if not (k == i and l == j) and 0 <= k < m and 0 <= l < n:
                    cur = sch[k][l]
                    if cur == "*":
                        return k, l
        return None

    ans = 0
    for i, row in enumerate(sch):
        nums = []
        gear_loc = None
        for j, col in enumerate(sch[i]):
            cur = sch[i][j]
            if cur.isnumeric():
                nums.append(sch[i][j])
                if not gear_loc:
                    gear_loc = star_search(i, j)
            else:
                if gear_loc:
                    stars[gear_loc].append(int("".join(nums)))
                nums.clear()
                gear_loc = None
        if gear_loc and nums:
            stars[gear_loc].append(int("".join(nums)))

    return sum(prod(starset) for starset in stars.values() if len(starset) == 2)


print(day_3a(IN_FILE_EX3))
print(day_3a(IN_FILE_PATH))
print(day_3b(IN_FILE_EX3))
print(day_3b(IN_FILE_PATH))

assert day_3a(IN_FILE_EX3) == 4361
assert day_3a(IN_FILE_PATH) == 535351
assert day_3b(IN_FILE_EX3) == 467835
assert day_3b(IN_FILE_PATH) == 87287096
