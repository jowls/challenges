from math import ceil, prod
from dataclasses import dataclass

IN_FILE_PATH = "advent_of_code/2023/day6/6.txt"
IN_FILE_EX = "advent_of_code/2023/day6/ex_6.txt"


@dataclass
class Race:
    time: int
    record: int


def parse_races(infile: str) -> list[Race]:
    """Parse races from file

    Args:
        infile: Input file path

    Returns:
        List of Races
    """
    with open(infile, "r") as file:
        _, time_line = file.readline().split(":")
        _, maxd_line = file.readline().split(":")
        time_vals = [int(x) for x in time_line.strip().split()]
        maxd_vals = [int(x) for x in maxd_line.strip().split()]
        return [Race(t, d) for t, d in zip(time_vals, maxd_vals)]


def day_6a(infile):
    races = parse_races(infile)
    ways = []

    for r in races:
        race_ways = 0
        st = ceil(r.record / r.time)
        en = r.time + 1
        for spd in range(st, en):
            d = spd * (r.time - spd)
            if d > r.record:
                race_ways += 1
        if race_ways:
            ways.append(race_ways)

    return prod(ways)


def day_6b(infile):
    races = parse_races(infile)
    time = dist = ""

    for r in races:
        time += str(r.time)
        dist += str(r.record)
    time, dist = [int(x) for x in [time, dist]]
    st = ceil(dist / time)
    en = time + 1
    ways = 0
    for spd in range(st, en):
        d = spd * (time - spd)
        if d > dist:
            ways += 1

    return ways


print(day_6a(IN_FILE_EX))
print(day_6a(IN_FILE_PATH))
print(day_6b(IN_FILE_EX))
print(day_6b(IN_FILE_PATH))

assert day_6a(IN_FILE_EX) == 288
assert day_6a(IN_FILE_PATH) == 861300
assert day_6b(IN_FILE_EX) == 71503
assert day_6b(IN_FILE_PATH) == 28101347
