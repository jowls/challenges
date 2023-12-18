IN_FILE_PATH = "advent_of_code/2023/day11/11.txt"
IN_FILE_EX = "advent_of_code/2023/day11/ex_11.txt"


class Image:
    def __init__(self, infile: str) -> None:
        self.data = self._parse_image_file(infile)
        self.empty_rows = self._find_empty_rows()
        self.empty_cols = self._find_empty_cols()
        self.galaxies = []

    @property
    def m(self):
        """Number of rows"""
        return len(self.data)

    @property
    def n(self):
        """Number of columns"""
        return len(self.data[0]) if self.data else 0

    def find_galaxies(self) -> None:
        """Populate galaxy list with coordinates"""
        for i in range(self.m):
            for j in range(self.n):
                if self.data[i][j] == "#":
                    self.galaxies.append((i, j))

    def calc_pair_dist_sum(self, multiplier: int) -> int:
        """Calculate the sum of Manhattan distances between all galaxy pairs"""
        dists = []
        for i, x in enumerate(self.galaxies):
            for j, y in enumerate(self.galaxies[i + 1 :]):
                dist = abs(y[1] - x[1]) + abs(y[0] - x[0])
                upper_bound_rows = max(x[0], y[0])
                lower_bound_rows = min(x[0], y[0])
                for k in self.empty_rows:
                    if lower_bound_rows < k < upper_bound_rows:
                        dist += multiplier - 1
                upper_bound_cols = max(x[1], y[1])
                lower_bound_cols = min(x[1], y[1])
                for k in self.empty_cols:
                    if lower_bound_cols < k < upper_bound_cols:
                        dist += multiplier - 1
                dists.append(dist)
        return sum(dists)

    def _parse_image_file(self, infile: str) -> list[list[str]]:
        with open(infile, "r") as file:
            data = [list(line.strip()) for line in file]
        return data

    def _find_empty_rows(self) -> list[int]:
        return [i for i, x in enumerate(self.data) if x.count(".") == len(x)]

    def _find_empty_cols(self) -> list[int]:
        return [
            j
            for j in range(self.n)
            if all(self.data[i][j] == "." for i in range(self.m))
        ]


def day_11a(infile):
    i = Image(infile)
    i.find_galaxies()

    return i.calc_pair_dist_sum(2)


def day_11b(infile):
    i = Image(infile)
    i.find_galaxies()

    return i.calc_pair_dist_sum(10**6)


print(day_11a(IN_FILE_EX))
print(day_11a(IN_FILE_PATH))
print(day_11b(IN_FILE_PATH))


assert day_11a(IN_FILE_EX) == 374
assert day_11a(IN_FILE_PATH) == 9681886
assert day_11b(IN_FILE_PATH) == 791134099634
