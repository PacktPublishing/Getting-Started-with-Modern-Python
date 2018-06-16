class Card(object):
    def __init__(self,cardSuit:int, cardVal:int):
        self._suit = cardSuit
        self._val = cardVal

    def get_suit_name(self) -> str:
        return ["SPADES", "DIAMONDS", "HEARTS", "CLUBS"][self._suit]

    def get_name(self) -> str:
        cardNames = "ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING".split()
        return cardNames[self._val]

    def get_short_name(self) -> str:
        return {0: 'A', 10: 'J', 11: 'Q', 12: 'K'}.get(
            self._val,
            str(self._val + 1)
        )

    def toString(self, abbreviate=True):
        if abbreviate:
            return self.get_short_name() + self.get_suit_name()[0]
        return "{card} of {suit}".format(card=self.get_name(), suit=self.get_suit_name())

    def get_points(self) -> int:
        if self._val == 0:
            return 11
        elif self._val >= 10:
            return 10
        return self._val + 1