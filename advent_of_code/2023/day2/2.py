from collections import defaultdict
from math import prod

IN_FILE_PATH = "advent_of_code/2023/day2/2.txt"
COLOUR_LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_games(infile: str) -> list[dict]:
    """Parse games from file

    Args:
        infile: Input file path

    Returns:
        List of games, each a dict with red/green/blue keys holding the max count observed
    """
    game_list = []
    with open(infile, "r") as file:
        for line in file:
            game_dict = defaultdict(int)
            _, grabs = line.strip().split(":")
            grabs = grabs.strip().split(";")
            for grab in grabs:
                grab_tokens = grab.split()
                for i in range(0, len(grab_tokens), 2):
                    colour = grab_tokens[i + 1].strip(",")
                    game_dict[colour] = max(
                        int(grab_tokens[i].strip()), game_dict[colour]
                    )
            game_list.append(game_dict)

    return game_list


def day_2a(infile):
    games = parse_games(infile)

    id_sum = 0
    for id, game in enumerate(games, 1):
        possible = True
        for colour, limit in COLOUR_LIMITS.items():
            if game[colour] > limit:
                possible = False
                break
        if possible:
            id_sum += id

    return id_sum


def day_2b(infile):
    return sum(prod(game.values()) for game in parse_games(infile))


print(day_2a(IN_FILE_PATH))
print(day_2b(IN_FILE_PATH))
assert day_2a(IN_FILE_PATH) == 2331
assert day_2b(IN_FILE_PATH) == 71585
