from math import inf

IN_FILE_PATH = "advent_of_code/2023/day5/5.txt"
IN_FILE_EX = "advent_of_code/2023/day5/ex_5.txt"


class Almanac:
    def __init__(self, seeds: list = None, maps: list = None) -> None:
        self.seeds = [] if not seeds else seeds
        self.maps = [] if not maps else maps

    def loc_from_seed(self, seed: int) -> int:
        cur = seed
        for map in self.maps:
            for (src, rng), dest in map.items():
                if src <= cur < src + rng:
                    offset = cur - src
                    cur = dest + offset
                    break
            # print(f"cur={cur}")

        return cur


def parse_almanac(infile: str) -> Almanac:
    """Parse almanac from file

    Args:
        infile: Input file path

    Returns:
        Almanac class
    """
    cards = []
    with open(infile, "r") as file:
        seeds = []
        al = Almanac()
        temp_map = {}
        for line in file:
            if not al.seeds:
                _, seeds = line.strip().split(":")
                al.seeds = [int(x) for x in seeds.strip().split()]
            else:
                if line == "\n":
                    if temp_map:
                        al.maps.append(temp_map.copy())
                        temp_map.clear()
                elif line[0].isalpha():
                    continue
                else:
                    des, src, rng = [int(x) for x in line.strip().split()]
                    temp_map[(src, rng)] = des
        if temp_map:
            al.maps.append(temp_map.copy())

    return al


def day_5a(infile):
    almanac = parse_almanac(infile)

    min_loc = inf
    for s in almanac.seeds:
        # print(f"seed={s}")
        loc = almanac.loc_from_seed(s)
        min_loc = min(loc, min_loc)
        # print(f"min_loc={min_loc}")

    return min_loc


def day_5b(infile):
    # TODO: brute force only, must revisit
    almanac = parse_almanac(infile)
    n = len(almanac.seeds)
    min_loc = inf
    for i in range(0, n, 2):
        st = almanac.seeds[i]
        rg = almanac.seeds[i + 1]
        for seed in range(st, st + rg):
            loc = almanac.loc_from_seed(seed)
            min_loc = min(loc, min_loc)
    return min_loc


print(day_5a(IN_FILE_EX))
print(day_5a(IN_FILE_PATH))
print(day_5b(IN_FILE_EX))
print(day_5b(IN_FILE_PATH))

assert day_5a(IN_FILE_EX) == 35
assert day_5a(IN_FILE_PATH) == 240320250
assert day_5b(IN_FILE_EX) == 46
assert day_5b(IN_FILE_PATH) == 28580589
