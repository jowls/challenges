IN_FILE_PATH = "advent_of_code/2024/day4/4.txt"
DIRECTIONS = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, -1),  # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),  # down-right
]


def parse_puzzle(infile: str) -> list[dict]:
    with open(infile, "r") as file:
        return [line.strip() for line in file]


def day_4a(infile):

    puzzle = parse_puzzle(infile)
    m = len(puzzle)
    n = len(puzzle[0])
    word = "XMAS"
    result = 0

    def search(row, col, depth, dx, dy):
        nonlocal result
        if puzzle[row][col] != word[depth]:
            return

        if depth == len(word) - 1:
            result += 1
            return

        search_row = row + dx
        search_col = col + dy

        if search_row >= 0 and search_col >= 0 and search_row < m and search_col < n:
            search(search_row, search_col, depth + 1, dx, dy)

    for row in range(m):
        for col in range(n):
            for dx, dy in DIRECTIONS:
                search(row, col, 0, dx, dy)

    return result


print(day_4a(IN_FILE_PATH))
# print(day_2b(IN_FILE_PATH))
assert day_4a(IN_FILE_PATH) == 2654
# assert day_2b(IN_FILE_PATH) == 71585
