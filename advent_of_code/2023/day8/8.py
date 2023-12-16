import re
from collections import defaultdict

IN_FILE_PATH = "advent_of_code/2023/day8/8.txt"
IN_FILE_EX = "advent_of_code/2023/day8/ex_8.txt"


def parse_maps(infile: str) -> (str, dict):
    """Parse directions and map network from file

    Args:
        infile: Input file path

    Returns:
        Directions and map network
    """

    network = defaultdict(list)

    with open(infile, "r") as file:
        dirs = file.readline().strip()
        file.readline()  # discard empty line
        pattern = re.compile("([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)")
        for line in file:
            matches = re.findall(pattern, line)
            network[matches[0][0]] = [matches[0][1], matches[0][2]]

    return dirs, network


def day_8a(infile):
    dirs, net = parse_maps(infile)

    cur = "AAA"
    i = 0
    n = len(dirs)
    while cur != "ZZZ":
        turn = dirs[i % n]
        cur = net[cur][0] if turn == "L" else net[cur][1]
        i += 1

    return i


print(day_8a(IN_FILE_EX))
print(day_8a(IN_FILE_PATH))

assert day_8a(IN_FILE_EX) == 2
assert day_8a(IN_FILE_PATH) == 13019
