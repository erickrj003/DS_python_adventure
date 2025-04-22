# Save/Load System class

import os
import pickle

class SaveLoad:
    """
    Save/Load System class that handles saving and loading game states.
    """
    
    def __init__(self, save_dir="saves"):
        """
        Initialize a new SaveLoad system.
        
        Args:
            save_dir (str): The directory to save games in
        """
        self.save_dir = save_dir
        self.save_file = "savegame.dat"
        
        # Create save directory if it doesn't exist
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        
        # TODO: Add support for multiple save slots
    
    def save_game(self, game_data):
        """
        Save game data to a file.
        
        Args:
            game_data (dict): The game data to save
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        save_path = os.path.join(self.save_dir, self.save_file)
        
        try:
            with open(save_path, 'wb') as file:
                pickle.dump(game_data, file)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
        
        # TODO: Add auto-save feature at key points (e.g., entering new areas)
    
    def load_game(self):
        """
        Load game data from a file.
        
        Returns:
            dict or None: The loaded game data, or None if load failed
        """
        save_path = os.path.join(self.save_dir, self.save_file)
        
        if not os.path.exists(save_path):
            return None
        
        try:
            with open(save_path, 'rb') as file:
                game_data = pickle.load(file)
            return game_data
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
    
    def has_saved_game(self):
        """
        Check if a saved game exists.
        
        Returns:
            bool: True if a saved game exists, False otherwise
        """
        save_path = os.path.join(self.save_dir, self.save_file)
        return os.path.exists(save_path)
    
    def delete_save(self):
        """
        Delete the saved game.
        
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        save_path = os.path.join(self.save_dir, self.save_file)
        
        if not os.path.exists(save_path):
            return True  # No save to delete
        
        try:
            os.remove(save_path)
            return True
        except Exception as e:
            print(f"Error deleting save: {e}")
            return False
            
    # TODO: Add method to display save metadata (player name, level, timestamp) 