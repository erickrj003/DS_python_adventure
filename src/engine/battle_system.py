# Battle System class

import random
import time

class BattleSystem:
    """
    Battle System class that handles combat encounters.
    """
    
    def __init__(self):
        """Initialize a new BattleSystem."""
        self.actions = ["attack", "use ability", "use item", "flee"]
        # TODO: Add more combat actions like "defend" to reduce damage or "special attack"
    
    def start_battle(self, player, enemy):
        """
        Start a battle between a player and an enemy.
        
        Args:
            player: The player character
            enemy: The enemy character
            
        Returns:
            str: The battle result ('victory', 'defeat', or 'fled')
        """
        print(f"\n=== BATTLE START: {player.name} vs. {enemy.name} ===")
        print(f"{enemy.name}: {enemy}")
        
        player_turn = True  # Player goes first
        
        # TODO: Implement initiative system to determine who goes first based on stats
        
        while player.is_alive() and enemy.is_alive():
            if player_turn:
                # Player's turn
                print(f"\n{player.name}'s turn...")
                print(f"Your HP: {player.health}/{player.max_health}")
                print(f"{enemy.name}'s HP: {enemy.health}/{enemy.max_health}")
                
                # Display available actions
                print("\nAvailable actions:")
                for i, action in enumerate(self.actions, 1):
                    print(f"{i}. {action.capitalize()}")
                
                # Get player's action
                action = self._get_player_action()
                
                if action == "attack":
                    damage = player.attack(enemy)
                    # TODO: Change the attack text to be weapon-specific (e.g. "You slash at the goblin with your sword!"). Perhaps generate custom text base on the power of your attack.
                    # TODO: Add critical hit chance based on random variables (dice roll, etc.)
                    # TODO Modify total damage based on enemy defense and armor
                    print(f"You attack {enemy.name} for {damage} damage!")
                    
                elif action == "use item":
                    # Get usable items from inventory
                    usable_items = [item for item in player.inventory if hasattr(item, "use")]
                    
                    if not usable_items:
                        print("You don't have any usable items!")
                        continue  # Skip turn
                    
                    # Display available items
                    print("\nAvailable items:")
                    for i, item in enumerate(usable_items, start=1):
                        print(f"{i}. {item.name}")
                    print(f"{len(usable_items) + 1}. Cancel")
                    
                    # Get player's choice
                    try:
                        choice = int(input("Choose an item to use: "))
                        if 1 <= choice <= len(usable_items):
                            selected_item = usable_items[choice - 1]
                            result = selected_item.use(player)
                            print(result)
                        else:
                            print("Action cancelled.")
                            continue  # Skip turn
                    except ValueError:
                        print("Invalid choice. Try again.")
                        continue  # Skip turn
                    
                elif action == "use ability":
                    # Get usable abilities from player character
                    usable_abilities = [ability for ability in player.abilities]
                    print("\nAvailable abilities:")
                    for i, ability in enumerate(usable_abilities, start=1):
                        print(f"{i}. {ability}")
                    print(f"{len(usable_abilities) + 1}. Cancel")

                    try:
                        choice = int(input("Choose an ability to use (enter number): "))
                        if 1 <= choice <= len(usable_abilities):
                            selected_ability = usable_abilities[choice - 1]
                            # use ability
                            ability_result = player.use_ability(selected_ability, enemy)
                            result = f"Selected ability was {selected_ability}. Use the ability here."  # Placeholder for ability usage logic
                            print(result)
                        else:
                            print("Invalid choice. Try again.")
                            continue
                    except ValueError:
                        print("Invalid choice. Try again.")
                        continue

                    if not usable_abilities:
                        print("You don't have any usable abilities!")
                        continue
                    
                
                elif action == "flee":
                    # 50% chance to flee
                    if random.random() < 0.5:
                        print(f"You successfully flee from {enemy.name}!")
                        return "fled"
                    else:
                        print(f"You failed to flee from {enemy.name}!")
                
                # Implement "defend" or "special attack" action here
            
            else:
                # Enemy's turn
                print(f"\n{enemy.name}'s turn...")
                time.sleep(0.5)  # Small delay for effect
                
                # TODO: Add basic AI for enemy combat decisions based on health
                
                damage, is_critical = enemy.attack(player)
                
                if is_critical:
                    print(f"{enemy.name} lands a CRITICAL HIT on you for {damage} damage!")
                else:
                    print(f"{enemy.name} attacks you for {damage} damage!")
            
            # Switch turns
            player_turn = not player_turn
            
            # Pause briefly between turns
            time.sleep(0.5)
        
        # Battle end
        print("\n=== BATTLE END ===")
        
        if player.is_alive():
            return "victory"
        else:
            return "defeat"
    
    def _get_player_action(self):
        """
        Get the player's battle action.
        
        Returns:
            str: The chosen action
        """
        while True:
            try:
                choice = input("Choose an action (enter number): ")
                choice = int(choice)
                
                if 1 <= choice <= len(self.actions):
                    return self.actions[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(self.actions)}.")
            except ValueError:
                print("Please enter a valid number.")
                
    # TODO: Add method for calculating critical hit chance based on character stats 