# Player class (inherits from Character)

from characters.character import Character

class Player(Character):
    """
    Player class that inherits from Character and adds player-specific
    attributes and behaviors.
    """
    
    def __init__(self, name, health=100, max_health=100, strength=15, defense=10):
        """
        Initialize a new Player.
        
        Args:
            name (str): The player's name
            health (int): Current health points
            max_health (int): Maximum health points  
            strength (int): Player's strength (affects damage)
            defense (int): Player's defense (reduces damage taken)
        """
        # Call the parent class constructor with player defaults
        super().__init__(name, health, max_health, strength, defense)
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.equipped_weapon = None
        self.equipped_armor = None
        self.current_location = None
        # TODO: Add player gold/currency attribute for buying items from merchants
        # TODO: Add player class attribute (warrior, mage, rogue) that affects gameplay overall (e.g. starting stats, available abilities, etc.)
    
    def gain_experience(self, amount):
        """
        Gain experience points and level up if necessary.
        
        Args:
            amount (int): The amount of experience to gain
            
        Returns:
            bool: True if the player leveled up, False otherwise
        """
        self.experience += amount
        level_up = False
        
        # Check if player has enough experience to level up
        while self.experience >= self.experience_to_next_level:
            self.level_up()
            level_up = True
            
        return level_up
    
    def level_up(self):
        """Level up the player, increasing their stats."""
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)
        
        # Increase stats
        old_max_health = self.max_health
        self.max_health += 10
        self.health += (self.max_health - old_max_health)  # Heal by the amount max health increased
        self.strength += 2
        self.defense += 1
        
        # TODO: Add different stat increases based on player class
        
        return f"Congratulations! You are now level {self.level}!"
    
    def equip_weapon(self, weapon):
        """
        Equip a weapon.
        
        Args:
            weapon: The weapon to equip
            
        Returns:
            object: The previously equipped weapon, if any
        """
        old_weapon = self.equipped_weapon
        self.equipped_weapon = weapon
        return old_weapon
    
    def equip_armor(self, armor):
        """
        Equip armor.
        
        Args:
            armor: The armor to equip
            
        Returns:
            object: The previously equipped armor, if any
        """
        old_armor = self.equipped_armor
        self.equipped_armor = armor
        return old_armor
    
    def attack(self, target):
        """
        Attack another character with current equipped weapon.
        
        Args:
            target (Character): The character to attack
            
        Returns:
            int: The amount of damage dealt
        """
        if not self.is_alive():
            return 0  # Can't attack if dead
        
        # Calculate damage based on strength and equipped weapon
        # TODO: add a random factor to the damage to simulate a more realistic attack (you could use the random module!)
        # TODO: add a random chance to miss the attack entirely or deal a critical hit (if the random factor is above a certain threshold)
        damage = self.strength
        if self.equipped_weapon:
            damage += self.equipped_weapon.damage_bonus
            
        return target.take_damage(damage)
    
    def take_damage(self, amount):
        """
        Take damage with armor protection.
        
        Args:
            amount (int): The amount of damage to take
            
        Returns:
            int: The actual damage taken after defense and armor
        """
        # Apply defense and armor to reduce damage
        defense_bonus = 0
        if self.equipped_armor:
            defense_bonus = self.equipped_armor.defense_bonus
            
        actual_damage = max(1, amount - self.defense - defense_bonus)
        self.health = max(0, self.health - actual_damage)
        return actual_damage
    
    def move_to(self, location):
        """
        Move to a new location.
        
        Args:
            location: The location to move to
        """
        self.current_location = location
    
    # TODO: Add method to allow player to buy items from merchants
    
    # TODO: Add special abilities based on player class
    
    def __str__(self):
        """Return string representation of the player."""
        base_str = super().__str__()
        return f"{base_str} [Level: {self.level}, XP: {self.experience}/{self.experience_to_next_level}]" 