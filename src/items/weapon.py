# Weapon class (inherits from Item)

from items.item import Item

class Weapon(Item):
    """
    Weapon class that inherits from Item and adds weapon-specific
    attributes and behaviors.
    """
    
    def __init__(self, name, description, value, damage_bonus):
        """
        Initialize a new Weapon.
        
        Args:
            name (str): The weapon's name
            description (str): The weapon's description
            value (int): The weapon's value in gold coins
            damage_bonus (int): The bonus damage the weapon provides
        """
        # Call the parent class constructor
        super().__init__(name, description, value)
        self.damage_bonus = damage_bonus
        self.equipped = False
    
    def use(self, character):
        """
        Equip the weapon to a character.
        
        Args:
            character: The character to equip the weapon to
            
        Returns:
            str: A message describing what happened
        """
        if hasattr(character, "equip_weapon"):
            old_weapon = character.equip_weapon(self)
            if old_weapon:
                old_weapon.equipped = False
                character.add_to_inventory(old_weapon)
                
            self.equipped = True
            if self in character.inventory:
                character.remove_from_inventory(self)
                
            return f"{character.name} equips {self.name}."
        else:
            return f"{character.name} can't equip weapons."
    
    def get_info(self):
        """
        Get detailed information about the weapon.
        
        Returns:
            str: Information about the weapon
        """
        base_info = super().get_info()
        return f"{base_info} [Damage Bonus: +{self.damage_bonus}]"
    
    def __eq__(self, other):
        """Check if two weapons are equal."""
        if not isinstance(other, Weapon):
            return False
        return (super().__eq__(other) and 
                self.damage_bonus == other.damage_bonus) 