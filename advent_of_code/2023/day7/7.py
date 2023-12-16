from math import prod
from collections import Counter

IN_FILE_PATH = "advent_of_code/2023/day7/7.txt"
IN_FILE_EX = "advent_of_code/2023/day7/ex_7.txt"


class Hand:
    card_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, cards: str, bid: str) -> None:
        self.cards = self._convert_hand(cards)
        self.freq = Counter(self.cards)
        self.typ = self._calc_type()
        self.bid = int(bid)
        self.rank = None

    def _convert_hand(self, hand: str) -> None:
        cards = []
        for card in hand:
            cards.append(int(card) if card.isnumeric() else self.card_map[card])
        return cards

    def _calc_type(self) -> None:
        cnts = sorted(self.freq.values(), reverse=True)
        match cnts[0]:
            case 5:
                return 7
            case 4:
                return 6
            case 3:
                return 5 if cnts[1] == 2 else 4  # check for full hosue
            case 2:
                return 3 if cnts[1] == 2 else 2  # check for one or two pair
            case 1:
                return 1


class Hands:
    def __init__(self, infile: str) -> None:
        self.hands = self._parse_hands(infile)

    def _parse_hands(self, infile: str):
        hands = []
        with open(infile, "r") as file:
            for line in file:
                hand, bid = line.split()
                hands.append(Hand(hand, bid))
        return hands

    def rank_hands(self) -> None:
        self.hands.sort(
            key=lambda h: (
                h.typ,
                h.cards[0],
                h.cards[1],
                h.cards[2],
                h.cards[3],
                h.cards[4],
            ),
            reverse=True,
        )
        n = len(self.hands)
        for i in range(n):
            self.hands[i].rank = n - i


def day_7a(infile):
    h = Hands(infile)
    h.rank_hands()
    return sum(x.rank * x.bid for x in h.hands)


print(day_7a(IN_FILE_EX))
print(day_7a(IN_FILE_PATH))

assert day_7a(IN_FILE_EX) == 6440
assert day_7a(IN_FILE_PATH) == 250898830
