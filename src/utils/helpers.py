# Helper functions

import random
import time
import os

def clear_screen():
    """Clear the console screen."""
    # Check the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac and Linux
        os.system('clear')

def roll_dice(num_dice=1, sides=6):
    """
    Roll dice and return the sum. Could be used for things like damage, healing, NPC interactions, etc.
    
    Args:
        num_dice (int): Number of dice to roll
        sides (int): Number of sides on each die
        
    Returns:
        int: The sum of the dice rolls
    """
    return sum(random.randint(1, sides) for _ in range(num_dice))