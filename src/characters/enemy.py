# Enemy class (inherits from Character)

from characters.character import Character
import random

class Enemy(Character):
    """
    Enemy class that inherits from Character and adds enemy-specific
    attributes and behaviors.
    """
    
    def __init__(self, name, health=50, max_health=50, strength=8, defense=3, 
                 level=1, experience_reward=10, loot_table=None):
        """
        Initialize a new Enemy.
        
        Args:
            name (str): The enemy's name
            health (int): Current health points
            max_health (int): Maximum health points
            strength (int): Enemy's strength (affects damage)
            defense (int): Enemy's defense (reduces damage taken)
            level (int): Enemy's level
            experience_reward (int): Experience points rewarded when defeated
            loot_table (list): Possible items that can be dropped
        """
        # Call the parent class constructor
        super().__init__(name, health, max_health, strength, defense)
        self.level = level
        self.experience_reward = experience_reward
        self.loot_table = loot_table or []
        
        # TODO: Add enemy type attribute (e.g., humanoid, beast, undead) for combat advantages/disadvantages
        
    def get_loot(self):
        """
        Get random loot from the enemy's loot table.
        
        Returns:
            object or None: A random item from the loot table, or None if no loot
        """
        if not self.loot_table:
            return None
            
        # Chance to drop nothing
        if random.random() < 0.3:  # 30% chance to drop nothing
            return None
            
        return random.choice(self.loot_table)
    
    def attack(self, target):
        """
        Attack another character, with a chance for a critical hit.
        
        Args:
            target (Character): The character to attack
            
        Returns:
            tuple: (damage dealt, whether it was a critical hit)
        """
        if not self.is_alive():
            return (0, False)
        
        # 10% chance for a critical hit (double damage)
        is_critical = random.random() < 0.1
        damage = self.strength
        
        if is_critical:
            damage *= 2
            
        actual_damage = target.take_damage(damage)
        return (actual_damage, is_critical)
    
    # TODO: Add special abilities for different enemy types
    
    def scale_to_level(self, level):
        """
        Scale enemy stats to match the given level.
        
        Args:
            level (int): The level to scale to
        """
        level_diff = level - self.level
        if level_diff <= 0:
            return  # Don't scale down
            
        self.level = level
        
        # Scale stats
        self.max_health += 10 * level_diff
        self.health = self.max_health
        self.strength += level_diff
        self.defense += level_diff // 2
        
        # Scale rewards
        self.experience_reward += 5 * level_diff
    
    # TODO: Add method for enemies to flee when low on health
        
    def __str__(self):
        """Return string representation of the enemy."""
        base_str = super().__str__()
        return f"{base_str} [Level: {self.level}, XP Reward: {self.experience_reward}]" 