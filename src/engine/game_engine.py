# Game Engine class

import sys
import time
from characters.player import Player
from world.world import World
from ui.user_interface import UserInterface
from engine.battle_system import BattleSystem
from engine.save_load import SaveLoad

class GameEngine:
    """
    Game Engine class that manages the game state and handles
    the main game loop.
    """
    
    def __init__(self):
        """Initialize a new GameEngine."""
        self.player = None
        self.world = World()
        self.ui = UserInterface()
        self.battle_system = BattleSystem()
        self.save_load = SaveLoad()
        self.running = False
        # TODO: Add quest system to track player progress
        # TODO: Add game time/day-night cycle that affects gameplay
    
    def start_game(self):
        """Start the game."""
        self.running = True
        self.ui.display_welcome()
        
        # Get player's choice
        choice = self.ui.get_main_menu_choice()
        
        if choice == "new":
            self.new_game()
        elif choice == "load":
            self.load_game()
        elif choice == "quit":
            self.ui.display_goodbye()
            self.running = False
            return
        
        # Main game loop
        self.game_loop()
    
    def new_game(self):
        """Start a new game."""
        # Get player name
        player_name = self.ui.get_player_name()
        
        # Create player
        self.player = Player(player_name)
        
        # Create game world
        self.world.create_world()
        
        # Set player's starting location
        self.player.move_to(self.world.get_starting_location())
        
        # Display introduction
        self.ui.display_introduction(self.player)
        
        # TODO: Add character class selection during new game
    
    def load_game(self):
        """Load a saved game."""
        # Check if there's a saved game
        if not self.save_load.has_saved_game():
            self.ui.display_message("No saved game found.")
            self.new_game()
            return
        
        # Load game data
        game_data = self.save_load.load_game()
        
        if game_data:
            self.player = game_data["player"]
            self.world = game_data["world"]
            self.ui.display_message(f"Welcome back, {self.player.name}!")
        else:
            self.ui.display_message("Failed to load game.")
            self.new_game()
    
    def save_game(self):
        """Save the current game."""
        game_data = {
            "player": self.player,
            "world": self.world
        }
        
        if self.save_load.save_game(game_data):
            self.ui.display_message("Game saved successfully.")
        else:
            self.ui.display_message("Failed to save game.")
    
    def game_loop(self):
        """Main game loop."""
        while self.running:
            # Check if player is alive
            if not self.player.is_alive():
                self.ui.display_message("You have died. Game over.")
                self.running = False
                break
            
            # Display current location
            current_location = self.player.current_location
            self.ui.display_location(current_location)
            
            # Check for enemies
            if current_location.has_enemies():
                # If there are multiple enemies, select one to encounter
                enemies = current_location.enemies
                enemy_count = len(enemies)
                
                if enemy_count > 1:
                    enemy_description = f"There are {enemy_count} enemies here! "
                    enemy_description += ", ".join([e.name for e in enemies[:-1]])
                    enemy_description += f" and {enemies[-1].name}."
                    self.ui.display_message(enemy_description)
                    
                # Choose the first enemy to fight
                enemy = enemies[0]
                self.ui.display_message(f"You encounter {enemy.name}!")
                self.ui.display_message(f"{enemy.name}: {enemy}")
                
                battle_result = self.battle_system.start_battle(self.player, enemy)
                
                if battle_result == "victory":
                    self.ui.display_message(f"You defeated {enemy.name}!")
                    
                    # Get experience
                    xp_reward = enemy.experience_reward
                    level_up = self.player.gain_experience(xp_reward)
                    self.ui.display_message(f"You gained {xp_reward} experience points.")
                    
                    if level_up:
                        self.ui.display_message(f"Congratulations! You are now level {self.player.level}!")
                        self.ui.display_message(f"Your health, strength, and defense have increased!")
                    
                    # Get loot
                    loot = enemy.get_loot()
                    if loot:
                        self.player.add_to_inventory(loot)
                        self.ui.display_message(f"You found {loot.name}!")
                        self.ui.display_message(loot.get_info())
                    else:
                        self.ui.display_message(f"The {enemy.name} didn't drop any loot.")
                    
                    # Remove enemy from location
                    current_location.remove_enemy(enemy)
                    
                    # Tell the player if there are still enemies in the area
                    if current_location.has_enemies():
                        remaining = len(current_location.enemies)
                        self.ui.display_message(f"There {'is' if remaining == 1 else 'are'} still {remaining} " +
                                                f"{'enemy' if remaining == 1 else 'enemies'} in the area.")
                    
                    # Display player's health after the battle
                    health_percentage = (self.player.health / self.player.max_health) * 100
                    health_status = f"Your health: {self.player.health}/{self.player.max_health} "
                    
                    if health_percentage <= 25:
                        health_status += "(LOW HEALTH! Consider using a healing item!)"
                    elif health_percentage <= 50:
                        health_status += "(You're injured. You might want to heal soon.)"
                    
                    self.ui.display_message(health_status)
                        
                elif battle_result == "defeat":
                    self.ui.display_message(f"You were defeated by {enemy.name}!")
                    self.running = False
                    break
                else:  # fled
                    self.ui.display_message(f"You fled from {enemy.name}!")
                    # Display player's health after fleeing
                    health_percentage = (self.player.health / self.player.max_health) * 100
                    health_status = f"Your health: {self.player.health}/{self.player.max_health} "
                    
                    if health_percentage <= 25:
                        health_status += "(LOW HEALTH! Consider using a healing item!)"
                    elif health_percentage <= 50:
                        health_status += "(You're injured. You might want to heal soon.)"
                    
                    self.ui.display_message(health_status)
            
            # TODO: Add random events that can occur while exploring
            
            # Get player command
            command = self.ui.get_command()
            
            # Process command
            self.process_command(command)

            # TODO: Add a delay between commands to simulate a more realistic game
            # TODO: Use a helper function to keep the game screen clean
    
    def process_command(self, command):
        """
        Process a player command.
        
        Args:
            command (str): The command to process
        """
        command = command.lower().strip()
        
        # Split command into parts
        parts = command.split()
        action = parts[0] if parts else ""
        args = parts[1:] if len(parts) > 1 else []
        
        # Process based on action
        if action in ["quit", "exit"]:
            self.ui.display_message("Are you sure you want to quit? (yes/no)")
            confirm = self.ui.get_input().lower()
            if confirm in ["yes", "y"]:
                self.running = False
        
        elif action == "help":
            self.ui.display_help()
        
        elif action == "look":
            # Do nothing since we already display look logic in the game loop
            pass

        elif action == "inventory" or action == "i":
            self.ui.display_inventory(self.player)
        
        elif action == "stats":
            self.ui.display_stats(self.player)
        
        elif action == "go" or action in ["north", "south", "east", "west", "up", "down"]:
            # Get direction
            direction = args[0] if action == "go" and args else action
            
            # Try to move in that direction
            new_location = self.player.current_location.get_connection(direction)
            
            if new_location:
                self.player.move_to(new_location)
                self.ui.display_message(f"You go {direction}.")
            else:
                self.ui.display_message(f"You can't go {direction} from here.")
        
        elif action == "take" or action == "get":
            if not args:
                self.ui.display_message("Take what?")
                return
                
            item_name = " ".join(args)
            location = self.player.current_location
            
            # Find the item
            target_item = None
            for item in location.items:
                if item.name.lower() == item_name.lower():
                    target_item = item
                    break
            
            if target_item:
                self.player.add_to_inventory(target_item)
                location.remove_item(target_item)
                self.ui.display_message(f"You take the {target_item.name}.")
            else:
                self.ui.display_message(f"There is no {item_name} here.")
        
        elif action == "drop":
            if not args:
                self.ui.display_message("Drop what?")
                return
                
            item_name = " ".join(args)
            
            # Find the item in inventory
            target_item = None
            for item in self.player.inventory:
                if item.name.lower() == item_name.lower():
                    target_item = item
                    break
            
            if target_item:
                self.player.remove_from_inventory(target_item)
                self.player.current_location.add_item(target_item)
                self.ui.display_message(f"You drop the {target_item.name}.")
            else:
                self.ui.display_message(f"You don't have a {item_name}.")
        
        elif action == "use":
            if not args:
                self.ui.display_message("Use what?")
                return
                
            item_name = " ".join(args)
            
            # Find the item in inventory
            target_item = None
            for item in self.player.inventory:
                if item.name.lower() == item_name.lower():
                    target_item = item
                    break
            
            if target_item:
                result = target_item.use(self.player)
                self.ui.display_message(result)
            else:
                self.ui.display_message(f"You don't have a {item_name}.")
        
        elif action == "talk":
            if not args:
                self.ui.display_message("Talk to whom?")
                return
                
            npc_name = " ".join(args)
            location = self.player.current_location
            
            # Find the NPC
            target_npc = None
            for npc in location.npcs:
                if npc.name.lower() == npc_name.lower():
                    target_npc = npc
                    break
            
            if target_npc:
                response = target_npc.talk()
                self.ui.display_message(f"{target_npc.name}: \"{response}\"")
            else:
                self.ui.display_message(f"There is no {npc_name} here.")
        
        elif action == "save":
            self.save_game()
            
        # TODO: Add 'buy' command for purchasing items from merchants
        
        # TODO: Add 'quest' command to view active quests
        
        else:
            self.ui.display_message(f"I don't understand '{command}'.")
            
    def quit_game(self):
        """Quit the game."""
        self.running = False
        self.ui.display_goodbye() 