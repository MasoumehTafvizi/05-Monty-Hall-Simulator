import random
from typing import Tuple

def monty_hall_game(switch_doors: bool) -> bool:
    """
    Simulate a single round of the Monty Hall game.

    :param switch_doors: Whether to switch doors after one is revealed.
    :return: True if the player wins, False otherwise.
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    
    initial_choice = random.choice(range(3))
    
    if switch_doors:
        doors_revealed = [i for i in range(3) if (i != initial_choice and doors[i] != 'car')]
        door_revealed = random.choice(doors_revealed)
        
        final_choice = [i for i in range(3) if (i != initial_choice and i != door_revealed)][0]
    else:
        final_choice = initial_choice
    
    return doors[final_choice] == 'car'


def simulate_game(num_games: int) -> Tuple[float, float]:
    """
        Simulate the Monty Hall game for a given number of games and calculate the winning probabilities for both strategies.

    :param num_games: The number of games to simulate.
    :return: A tuple containing the winning probabilities for not switching and switching strategies, respectively.
    """
    num_wins_without_switching = sum(monty_hall_game(False) for _ in range(num_games))
    num_wins_with_switching = sum(monty_hall_game(True) for _ in range(num_games))
    
    return num_wins_without_switching/num_games, num_wins_with_switching/num_games


if __name__ == '__main__':
    num_games = 10000
    num_wins_without_switching,num_wins_with_switching = simulate_game(num_games)
    print(f"Winning probability without switching: {num_wins_without_switching:.2%}")
    print(f"Winning probability with switching: {num_wins_with_switching:.2%}")