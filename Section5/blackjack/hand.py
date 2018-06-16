from typing import List

from Section5.blackjack import Card


class Hand(object):
    def __init__(self):
        self._cards: List[Card] = []
        self._total = None

    @property
    def score(self):
        return self._total

    def add_card(self,*cards: Card):
        for card in cards:
            self._cards.append(card)
        if self.recalculate_hand_score() > 21:
            raise Exception("BUST!!!!")
        return self

    def recalculate_hand_score(self):
        total = 0
        aces = 0
        for card in self._cards:
            total += card.get_points()
            aces += int(card._val == 0)  # int(True) is 1
        while aces > 0 and total > 21:
            aces -= 1
            total -= 10
        self._total = total
        return total

    def toString(self) -> str:
        cards = ("[ {card} ]".format(card=c.toString()) for c in self._cards)
        return "  ".join(cards)
