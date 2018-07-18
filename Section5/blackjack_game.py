import random

from Section5.blackjack import Card
from Section5.blackjack import Hand
from Section5.functions01 import get_valid_input


class BlackjackGame(object):
    dealer = None
    player = None
    deck   = None

    def shuffle(self):
        self.deck = [Card( suit,val) for val in range(13) for suit in range(4)]
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        self.player = Hand().add_card(self.deck.pop(0), self.deck.pop(0), )
        self.dealer = Hand().add_card(self.deck.pop(0), self.deck.pop(0), )

    def ask_player_hit_or_stay(self):
        input_validator = lambda inp: inp.lower()[0] in "hs"
        prompt = "[H]it or [S]tand?"
        error_msg = "Please enter [H]it or [S]tand"
        return get_valid_input(prompt, error_msg, input_validator)

    def play(self):
        self.deal()
        print("Dealer Shows:", self.dealer._cards[0].toString(False))
        print("You Have: ", self.player.toString())
        action = self.ask_player_hit_or_stay()
        while action.lower().startswith("h"):
            try:
                self.player.add_card(self.deck.pop(0))
            except Exception as e:
                print("You Draw:", self.player._cards[-1].toString(False))
                print("PLAYER BUSTS!!!")
            else:
                print("You Draw:", self.player._cards[-1].toString(False))
                print("You Have: ", self.player.toString())
                print("Score:", self.player.score)
                action = self.ask_player_hit_or_stay()
        while self.dealer.score < 17:
            try:
                self.dealer.add_card(self.deck.pop(0))
            except:
                print("DEALER BUSTS!!!!")

        print("DEALER:",self.dealer.toString())
        print("PLAYER:",self.player.toString())
    def MainLoop(self):
        self.play()
        while input("play again?").lower().startswith("y"):
            self.play()

if __name__ == "__main__":
    BlackjackGame().MainLoop()