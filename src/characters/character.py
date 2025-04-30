# Character Base Class

class Character:
    """
    Base Character class that defines common attributes and behaviors
    for all characters in the game world.
    """
    
    def __init__(self, name, health=100, max_health=100, strength=10, defense=5):
        """
        Initialize a new Character.
        
        Args:
            name (str): The character's name
            health (int): Current health points
            max_health (int): Maximum health points
            strength (int): Character's strength (affects damage)
            defense (int): Character's defense (reduces damage taken)
        """
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.defense = defense
        self.inventory = [] 
        self.char_class = "Character"  # Default class type
        
    def is_alive(self):
        """Check if the character is alive."""
        return self.health > 0
    
    def take_damage(self, amount):
        """
        Take damage and update health.
        
        Args:
            amount (int): The amount of damage to take
            
        Returns:
            int: The actual damage taken after defense is applied
        """
        # Apply defense to reduce damage (minimum 1 damage if hit)
        actual_damage = max(1, amount - self.defense)
        self.health = max(0, self.health - actual_damage)
        return actual_damage
    
    def heal(self, amount):
        """
        Heal the character.
        
        Args:
            amount (int): The amount of health to restore
            
        Returns:
            int: The actual amount healed
        """
        if self.health <= 0:
            return 0  # Can't heal if dead
            
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        return self.health - old_health
    
    def attack(self, target):
        """
        Attack another character.
        
        Args:
            target (Character): The character to attack
            
        Returns:
            int: The amount of damage dealt
        """
        if not self.is_alive():
            return 0  # Can't attack if dead
        
        damage = self.strength  # Base damage = strength
        return target.take_damage(damage)
    
    def add_to_inventory(self, item):
        """
        Add an item to the character's inventory.
        
        Args:
            item: The item to add
        """
        self.inventory.append(item)
    
    def remove_from_inventory(self, item):
        """
        Remove an item from the character's inventory.
        
        Args:
            item: The item to remove
            
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def __str__(self):
        """Return string representation of the character."""
        return f"{self.name} (HP: {self.health}/{self.max_health}, STR: {self.strength}, DEF: {self.defense})" 