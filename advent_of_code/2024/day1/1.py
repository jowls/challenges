from collections import defaultdict

IN_FILE_PATH = "advent_of_code/2024/day1/1.txt"


def day_1a(infile):
    with open(infile, "r") as file:
        lines = file.readlines()

    map0 = []
    map1 = []
    for line in lines:
        map_parts = line.split()
        map0.append(int(map_parts[0]))
        map1.append(int(map_parts[1]))

    diff = 0
    map0.sort()
    map1.sort()

    for i in range(len(map0)):
        diff += abs(map0[i] - map1[i])

    return diff


def day_1b(infile):
    with open(infile, "r") as file:
        lines = file.readlines()

    map0 = []
    map1 = []
    similarity = defaultdict(int)
    for line in lines:
        map_parts = line.split()
        map0.append(int(map_parts[0]))
        map1.append(int(map_parts[1]))

    for i in range(len(map0)):
        if map1[i] in map0:
            similarity[map1[i]] += 1

    return sum(k * v for k, v in similarity.items())


print(day_1a(IN_FILE_PATH))
print(day_1b(IN_FILE_PATH))
assert day_1a(IN_FILE_PATH) == 936063
assert day_1b(IN_FILE_PATH) == 23150395
