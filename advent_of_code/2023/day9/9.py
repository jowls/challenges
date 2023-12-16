IN_FILE_PATH = "advent_of_code/2023/day9/9.txt"
IN_FILE_EX = "advent_of_code/2023/day9/ex_9.txt"


def parse_report(infile: str) -> list[list[int]]:
    """Parse oasis report from file

    Args:
        infile: Input file path

    Returns:
        Oasis report
    """

    rep = []

    with open(infile, "r") as file:
        for line in file:
            rep.append([int(x) for x in line.strip().split()])

    return rep


def calc_seqs(seq: list[int]) -> list[list[int]]:
    """Calculate all intermediate diff sequences from inital

    Args:
        seq: Input sequence

    Returns:
        All diff sequences until 0
    """

    seqs = [seq]

    while any(seqs[-1]):  # if not all zeroes
        prv = seqs[-1]
        cur = [prv[i] - prv[i - 1] for i in range(1, len(prv))]
        seqs.append(cur)

    return seqs


def day_9a(infile):
    rep = parse_report(infile)
    ans = 0
    for line in rep:
        seqs = calc_seqs(line)
        seqs[-1].append(0)
        seq_depth = len(seqs)
        for i in range(seq_depth - 2, -1, -1):
            seqs[i].append(seqs[i][-1] + seqs[i + 1][-1])
        ans += seqs[0][-1]
    return ans


def day_9b(infile):
    rep = parse_report(infile)
    ans = 0
    for line in rep:
        seqs = calc_seqs(line)
        seqs[-1].insert(0, 0)
        seq_depth = len(seqs)
        for i in range(seq_depth - 2, -1, -1):
            seqs[i].insert(0, seqs[i][0] - seqs[i + 1][0])
        ans += seqs[0][0]
    return ans


print(day_9a(IN_FILE_EX))
print(day_9a(IN_FILE_PATH))
print(day_9b(IN_FILE_PATH))

assert day_9a(IN_FILE_EX) == 114
assert day_9a(IN_FILE_PATH) == 2175229206
assert day_9b(IN_FILE_PATH) == 942
