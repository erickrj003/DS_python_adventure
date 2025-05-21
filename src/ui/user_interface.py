# User Interface class

class UserInterface:
    """
    User Interface class that handles the game's text-based interface.
    """
    
    def __init__(self):
        """Initialize a new UserInterface."""
        self.width = 80  # Width of the UI elements
        # TODO: Add color support for different message types (combat, items, etc.)
    
    def display_welcome(self):
        """Display the welcome screen."""
        self._display_header("WELCOME TO MR. JOHNSON'S FANTASY ADVENTURE!")
        print("Welcome to Mr. Johnson's Text-Based RPG Adventure!")
        print("Explore the world, battle enemies, and become a hero.\n")
        print("This mini-project is the final grade for Mooseheart Data Structures Students.")
        print("There are several TODOs that need to be completed before this game is finished.")
        print("The current version is 0.2.2. When you accomplish TODOs, the version will increment.")
        print("=" * self.width)
    
    def get_main_menu_choice(self):
        """
        Get the player's main menu choice.
        
        Returns:
            str: The player's choice ("new", "load", or "quit")
        """
        print("\nMain Menu:")
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                return "new"
            elif choice == "2":
                return "load"
            elif choice == "3":
                return "quit"
            else:
                print("Invalid choice. Please try again.")
    
    def get_player_name(self):
        """
        Get the player's name.
        
        Returns:
            str: The player's name
        """
        while True:
            name = input("\nEnter your character's name: ")
            
            if name and len(name) <= 20:
                return name
            else:
                print("Please enter a valid name (1-20 characters).")
    
    def display_introduction(self, player):
        """
        Display the game introduction.
        
        Args:
            player: The player character
        """
        self._display_header("INTRODUCTION")
        print(f"Welcome, {player.name}!")

        skip_intro = input("Are you a returning player? yes or no?")
        if skip_intro == 'yes':
            print("You skipped the intro. Welcome back!")
            print("="* self.width)
            input("\nPress Enter to continue your adventure")
            return 
        
        print("You find yourself in a small medieval town, ready to start your adventure.")
        print("Explore the world, complete quests, and battle enemies to become a hero.")
        print("Type 'help' at any time to see available commands.")
        print("=" * self.width)
        input("\nPress Enter to begin your adventure...")
        
        # TODO: Add option to skip introduction for returning players
        
    
    def display_location(self, location, world):
        """
        Display the current location.
        
        Args:
            location: The current location
        """
        self._display_header(location.name)
        print(location.get_description())
        if (world.time_minutes >= 70 and world.time_minutes <= 120):
            print("It is Morning.")
        elif (world.time_minutes > 120 and world.time_minutes <= 160):
            print("It is Afternoon.")
        elif (world.time_minutes > 160 and world.time_minutes <= 200):
            print("It is Evening.")
        elif (world.time_minutes > 200 and world.time_minutes <= 0):
            print("It is Dusk.")
        elif (world.time_minutes > 0 and world.time_minutes <= 40):
            print("It is Late Night.")
        elif (world.time_minutes > 40 and world.time_minutes <= 60):
            print("It is Dawn.")
        print(world.time_minutes)
    
    def display_inventory(self, player):
        """
        Display the player's inventory.
        
        Args:
            player: The player character
        """
        self._display_header("INVENTORY")
        
        if not player.inventory:
            print("Your inventory is empty.")
            return
        
        for i, item in enumerate(player.inventory, 1):
            item_type = type(item).__name__
            equipped = ""
            
            if hasattr(item, "equipped") and item.equipped:
                equipped = " (Equipped)"
            
            print(f"{i}. {item.name}{equipped} - {item_type}")
        
        # TODO: Add functionality to use or equip items directly from inventory display
    
    def display_stats(self, player):
        """
        Display the player's stats.
        
        Args:
            player: The player character
        """
        self._display_header("CHARACTER STATS")
        print(f"Name: {player.name}")
        print(f"Level: {player.level}")
        print(f"Experience: {player.experience}/{player.experience_to_next_level}")
        print(f"Health: {player.health}/{player.max_health}")
        print(f"Strength: {player.strength}")
        print(f"Defense: {player.defense}")
        
        if player.equipped_weapon:
            print(f"Weapon: {player.equipped_weapon.name} (+{player.equipped_weapon.damage_bonus} damage)")
        else:
            print("Weapon: None")
            
        if player.equipped_armor:
            print(f"Armor: {player.equipped_armor.name} (+{player.equipped_armor.defense_bonus} defense)")
        else:
            print("Armor: None")
        
        # TODO: Add visual HP bar to make health status more clear
    
    def display_help(self):
        """Display the help screen with available commands."""
        self._display_header("HELP")
        
        commands = [
            ("look", "Look around the current location"),
            ("go <direction>", "Move in the specified direction (north, south, east, west, up, down)"),
            ("inventory", "Show your inventory"),
            ("stats", "Show your character stats"),
            ("take <item>", "Take an item from the current location"),
            ("drop <item>", "Drop an item from your inventory"),
            ("use <item>", "Use an item from your inventory"),
            ("talk <npc>", "Talk to an NPC in the current location"),
            ("save", "Save your game"),
            ("help", "Show this help screen"),
            ("quit", "Exit the game")
        ]
        
        for cmd, desc in commands:
            print(f"{cmd.ljust(20)} - {desc}")
        
        # TODO: Add 'buy' and 'quest' commands to help screen when implemented
    
    def display_message(self, message):
        """
        Display a message to the player.
        
        Args:
            message (str): The message to display
        """
        print(f"\n{message}")
    
    def get_command(self):
        """
        Get a command from the player.
        
        Returns:
            str: The player's command
        """
        return input("\n> ").strip()
    
    def get_input(self, prompt=None):
        """
        Get input from the player.
        
        Args:
            prompt (str, optional): The prompt to display
            
        Returns:
            str: The player's input
        """
        if prompt:
            return input(prompt).strip()
        else:
            return input().strip()
    
    def display_goodbye(self):
        """Display the goodbye message."""
        print("\nThank you for playing!")
    
    def _display_header(self, title):
        """
        Display a header with the given title.
        
        Args:
            title (str): The title to display
        """
        print("\n" + "=" * self.width)
        print(title.center(self.width))
        print("=" * self.width + "\n")
        
    # TODO: Add a map display function to show nearby locations visually 