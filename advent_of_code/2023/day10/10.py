from collections import defaultdict
from math import inf
import sys

IN_FILE_PATH = "advent_of_code/2023/day10/10.txt"
IN_FILE_EX = "advent_of_code/2023/day10/ex_10.txt"
sys.setrecursionlimit(15000)


def parse_pipes(infile: str) -> list[list[str]]:
    """Parse pipe map from file"""

    with open(infile, "r") as file:
        pipe_map = [[x for x in line.strip()] for line in file]

    return pipe_map


def find_start(pipe_map: list[list[str]]) -> tuple(int, int):
    """Return coordinates of S"""
    m = len(pipe_map)
    n = len(pipe_map[0])

    for i in range(m):
        for j in range(n):
            if pipe_map[i][j] == "S":
                return i, j


def calc_start_pipe(i: int, j: int, pipe_map: list[list[str]]) -> str:
    """Determine the type of the starting pipe"""
    n = s = e = w = False
    if i - 1 >= 0:
        if pipe_map[i - 1][j] in {"|", "F", "7"}:
            n = True
    if i + 1 < len(pipe_map):
        if pipe_map[i + 1][j] in {"|", "J", "L"}:
            s = True
    if j - 1 >= 0:
        if pipe_map[i][j - 1] in {"-", "F", "L"}:
            w = True
    if j + 1 < len(pipe_map[0]):
        if pipe_map[i][j + 1] in {"-", "J", "7"}:
            e = True
    if n and s:
        return "|"
    if e and w:
        return "-"
    if n and e:
        return "L"
    if n and w:
        return "J"
    if e and s:
        return "F"
    if w and s:
        return "7"


def day_10a(infile):
    pipe_map = parse_pipes(infile)
    i, j = find_start(pipe_map)
    pipe_map[i][j] = calc_start_pipe(i, j, pipe_map)
    m = len(pipe_map)
    n = len(pipe_map[0])
    visited = defaultdict(lambda: inf)
    dirs = {
        "F": [(1, 0), (0, 1)],
        "7": [(1, 0), (0, -1)],
        "J": [(-1, 0), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "-": [(0, -1), (0, 1)],
        "|": [(1, 0), (-1, 0)],
    }

    def dfs(i: int, j: int, depth: int) -> None:
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or pipe_map[i][j] == "."
            or visited[(i, j)] <= depth
        ):
            return

        visited[(i, j)] = depth

        for di, dj in dirs[pipe_map[i][j]]:
            dfs(i + di, j + dj, depth + 1)

    dfs(i, j, 0)
    return max(x for x in visited.values())


print(day_10a(IN_FILE_EX))
print(day_10a(IN_FILE_PATH))

assert day_10a(IN_FILE_EX) == 8
assert day_10a(IN_FILE_PATH) == 6968
