IN_FILE_PATH = "advent_of_code/2024/day2/2.txt"


def parse_reports(infile: str) -> list[dict]:
    with open(infile, "r") as file:
        return [[int(x) for x in line.strip().split()] for line in file]


def is_safe(reports):
    return is_safe_ascending(reports) or is_safe_descending(reports)


def is_safe_descending(report):
    return all(x > y and abs(x - y) <= 3 for x, y in zip(report, report[1:]))


def is_safe_ascending(report):
    return all(x < y and abs(x - y) <= 3 for x, y in zip(report, report[1:]))


def day_2a(infile):
    reports = parse_reports(infile)
    return sum(1 for r in reports if is_safe(r))


print(day_2a(IN_FILE_PATH))
# print(day_2b(IN_FILE_PATH))
assert day_2a(IN_FILE_PATH) == 442
# assert day_2b(IN_FILE_PATH) == 71585
