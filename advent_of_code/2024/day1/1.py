from collections import defaultdict

IN_FILE_PATH = "advent_of_code/2024/day1/1.txt"


def parse_list_data(infile):
    with open(infile, "r") as file:
        return [tuple(map(int, line.split())) for line in file]


def day_1a(infile):
    list_data = parse_list_data(IN_FILE_PATH)

    list0, list1 = zip(*list_data)
    list0, list1 = sorted(list0), sorted(list1)

    return sum(abs(a - b) for a, b in zip(list0, list1))


def day_1b(infile):
    list_data = parse_list_data(IN_FILE_PATH)

    list0, list1 = zip(*list_data)

    similarity = defaultdict(int)
    for i in range(len(list0)):
        if list1[i] in list0:
            similarity[list1[i]] += 1

    return sum(k * v for k, v in similarity.items())


print(day_1a(IN_FILE_PATH))
print(day_1b(IN_FILE_PATH))
assert day_1a(IN_FILE_PATH) == 936063
assert day_1b(IN_FILE_PATH) == 23150395
