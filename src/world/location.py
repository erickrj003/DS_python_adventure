# Location class

class Location:
    """
    Location class that represents areas in the game world.
    """
    
    def __init__(self, name, description):
        """
        Initialize a new Location.
        
        Args:
            name (str): The location's name
            description (str): The location's description
        """
        self.name = name
        self.description = description
        self.npcs = []
        self.enemies = []
        self.items = []
        self.connections = {}  # Dictionary mapping direction to connected location
        
    def add_connection(self, direction, location):
        """
        Add a connection to another location.
        
        Args:
            direction (str): The direction of the connection (e.g., 'north', 'south')
            location: The location the connection leads to
        """
        self.connections[direction] = location
    
    def get_connection(self, direction):
        """
        Get the location in the specified direction.
        
        Args:
            direction (str): The direction to move
            
        Returns:
            Location or None: The connected location or None if no connection
        """
        return self.connections.get(direction)
    
    def get_available_directions(self):
        """
        Get all available directions from this location.
        
        Returns:
            list: List of directions that have connections
        """
        return list(self.connections.keys())
    
    def add_npc(self, npc):
        """
        Add an NPC to the location.
        
        Args:
            npc: The NPC to add
        """
        self.npcs.append(npc)
    
    def add_enemy(self, enemy):
        """
        Add an enemy to the location.
        
        Args:
            enemy: The enemy to add
        """
        self.enemies.append(enemy)
    
    def add_item(self, item):
        """
        Add an item to the location.
        
        Args:
            item: The item to add
        """
        self.items.append(item)
    
    def remove_item(self, item):
        """
        Remove an item from the location.
        
        Args:
            item: The item to remove
            
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def remove_enemy(self, enemy):
        """
        Remove an enemy from the location.
        
        Args:
            enemy: The enemy to remove
            
        Returns:
            bool: True if the enemy was removed, False otherwise
        """
        if enemy in self.enemies:
            self.enemies.remove(enemy)
            return True
        return False
    
    def has_enemies(self):
        """
        Check if the location has enemies.
        
        Returns:
            bool: True if the location has enemies, False otherwise
        """
        return len(self.enemies) > 0
    
    def get_description(self):
        """
        Get a complete description of the location.
        
        Returns:
            str: A description of the location and its contents
        """
        desc = f"=== {self.name} ===\n"
        desc += f"{self.description}\n"
        
        # Add information about items
        if self.items:
            desc += "\nItems here:\n"
            for item in self.items:
                desc += f"- {item.name}\n"
        
        # Add information about NPCs
        if self.npcs:
            desc += "\nNPCs here:\n"
            for npc in self.npcs:
                desc += f"- {npc.name}\n"
        
        # Add information about enemies
        if self.enemies:
            desc += "\nEnemies here:\n"
            for enemy in self.enemies:
                desc += f"- {enemy.name}\n"
        
        # Add information about exits
        if self.connections:
            desc += "\nExits:\n"
            for direction, location in self.connections.items():
                desc += f"- {direction.capitalize()}: {location.name}\n"
        
        return desc
    
    def __str__(self):
        """Return string representation of the location."""
        return self.name 