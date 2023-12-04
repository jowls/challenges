IN_FILE_PATH = "advent_of_code/2023/day4/4.txt"
IN_FILE_EX = "advent_of_code/2023/day4/ex_4.txt"


def parse_cards(infile: str) -> list[dict]:
    """Parse scratch card numbers from file

    Args:
        infile: Input file path

    Returns:
        List of dicts containing win numbers and numbers you have
    """
    cards = []
    with open(infile, "r") as file:
        for line in file:
            _, all_nums = line.strip().split(":")
            win, have = [
                set(int(num) for num in x.strip().split())
                for x in all_nums.strip().split("|")
            ]
            cards.append({"win": win, "have": have})

    return cards


def card_value(card: dict) -> int:
    """Calculates point value of cards according to original problem description

    Args:
        card: Card dictionary

    Returns:
        Number of points the card is worth
    """
    points = 0
    for num in card["have"]:
        if num in card["win"]:
            points = points * 2 if points else 1
    return points


def true_card_value(card: dict) -> int:
    """Calculate next cards won according to actual rules found on back of card

    Args:
        card: Card dictionary

    Returns:
        Number of points the card is worth
    """
    points = 0
    for num in card["have"]:
        if num in card["win"]:
            points += 1
    return points


def day_4a(infile):
    cards = parse_cards(infile)

    return sum(card_value(card) for card in cards)


def day_4b(infile):
    cards = parse_cards(infile)
    tab = []
    ans = 0
    for card in reversed(cards):
        pts = true_card_value(card)
        tab.append((len(tab[-pts:]) + sum(tab[-pts:]) if pts else 0))

    return sum(tab) + len(tab)


print(day_4a(IN_FILE_EX))
print(day_4a(IN_FILE_PATH))
print(day_4b(IN_FILE_EX))
print(day_4b(IN_FILE_PATH))

assert day_4a(IN_FILE_EX) == 13
assert day_4a(IN_FILE_PATH) == 26443
assert day_4b(IN_FILE_EX) == 30
assert day_4b(IN_FILE_PATH) == 6284877
