import random
from typing import List, Dict, Tuple

def greet(adventurer: str) -> str:
    """
    returns a greeting string that greets the title cased adventurers name

    >>> greet('bob')
    'Hello Brave Bob'

    :param adventurer: the name of the adventurer to greet
    :return: a greeting "Hello ..."
    """
    return f"Hello Brave {adventurer.title()}"

def roll_dice(n_dice:int=1,n_sides:int=6)->List[int]:
    """
    roll N dice(each with X sides) and return the results

    >>> random.seed(123)
    >>> roll_dice(3)
    [1, 3, 1]
    >>> roll_dice(4, 20)
    [14, 9, 4, 2]

    :param n_dice:  number of dice to roll
    :param n_sides: number of sides on each dice
    :return: a list of all dice rolls
    """
    return [random.randint(1,n_sides) for _ in range(n_dice)]

Player = Dict[str, int]
def encounter(player: Player,monster: Player) -> int:
    """
    A battle encounter between the player and a monster
    *note that the monster may be another player*

    :param player: the PlayerInstance
    :param monster: the MobInstance that the player is fighting
    :return: 1 if the player wins; -1 if player loses; 0 for a draw
    """
    pass

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]
def broadcast(message: str, servers: List[Server]) -> None:
    """
    send a message to various server endpoints


    :param message: the message to send to the endpoints
    :param servers: a list of Server endpoints ((Address,connectionOpts)
    :return: None
    """
    pass

if __name__ == "__main__":
    print(help(broadcast))