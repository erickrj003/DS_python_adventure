# Main Game Entry Point

from engine.game_engine import GameEngine # from the engine folder, find the game_engine.py file and get the class "GameEngine" from it

def main():
    """Main entry point for arguments to enable debug mode or skip intro (when main.py is run)
     the game."""
    # TODO: Add command line
    # Initialize the game engine
    game = GameEngine()
    
    # Start the game
    game.start_game()

if __name__ == "__main__":
    main() 