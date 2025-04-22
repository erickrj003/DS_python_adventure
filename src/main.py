# Main Game Entry Point

from engine.game_engine import GameEngine

def main():
    """Main entry point for the game."""
    # TODO: Add command line arguments to enable debug mode or skip intro (when main.py is run)
    
    # Initialize the game engine
    game = GameEngine()
    
    # Start the game
    game.start_game()

if __name__ == "__main__":
    main() 