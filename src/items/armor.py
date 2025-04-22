# Armor class (inherits from Item)

from items.item import Item

class Armor(Item):
    """
    Armor class that inherits from Item and adds armor-specific
    attributes and behaviors.
    """
    
    def __init__(self, name, description, value, defense_bonus):
        """
        Initialize a new Armor.
        
        Args:
            name (str): The armor's name
            description (str): The armor's description
            value (int): The armor's value in gold coins
            defense_bonus (int): The bonus defense the armor provides
        """
        # Call the parent class constructor
        super().__init__(name, description, value)
        self.defense_bonus = defense_bonus
        self.equipped = False
    
    def use(self, character):
        """
        Equip the armor to a character.
        
        Args:
            character: The character to equip the armor to
            
        Returns:
            str: A message describing what happened
        """
        if hasattr(character, "equip_armor"):
            old_armor = character.equip_armor(self)
            if old_armor:
                old_armor.equipped = False
                character.add_to_inventory(old_armor)
                
            self.equipped = True
            if self in character.inventory:
                character.remove_from_inventory(self)
                
            return f"{character.name} equips {self.name}."
        else:
            return f"{character.name} can't equip armor."
    
    def get_info(self):
        """
        Get detailed information about the armor.
        
        Returns:
            str: Information about the armor
        """
        base_info = super().get_info()
        return f"{base_info} [Defense Bonus: +{self.defense_bonus}]"
    
    def __eq__(self, other):
        """Check if two armors are equal."""
        if not isinstance(other, Armor):
            return False
        return (super().__eq__(other) and 
                self.defense_bonus == other.defense_bonus) 