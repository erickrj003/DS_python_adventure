# Consumable class (inherits from Item)

from items.item import Item

class Consumable(Item):
    """
    Consumable class that inherits from Item and adds consumable-specific
    attributes and behaviors.
    """
    
    def __init__(self, name, description, value, effect_type, effect_value):
        """
        Initialize a new Consumable.
        
        Args:
            name (str): The consumable's name
            description (str): The consumable's description
            value (int): The consumable's value in gold coins
            effect_type (str): The type of effect ('health', 'strength', etc.)
            effect_value (int): The value of the effect
        """
        # Call the parent class constructor
        super().__init__(name, description, value)
        self.effect_type = effect_type
        self.effect_value = effect_value
        # TODO: Add duration for temporary stat boost effects
    
    def use(self, character):
        """
        Use the consumable on a character.
        
        Args:
            character: The character using the consumable
            
        Returns:
            str: A message describing what happened
        """
        if not character.is_alive():
            return f"{character.name} is not alive and cannot use {self.name}."
            
        message = f"{character.name} uses {self.name}."
        
        # Apply the effect based on its type
        if self.effect_type == "health":
            amount_healed = character.heal(self.effect_value)
            message += f" {character.name} is healed for {amount_healed} health."
        
        elif self.effect_type == "strength":
            character.strength += self.effect_value
            message += f" {character.name}'s strength increases by {self.effect_value}."
        
        elif self.effect_type == "defense":
            character.defense += self.effect_value
            message += f" {character.name}'s defense increases by {self.effect_value}."
        
        elif self.effect_type == "critical chance":
            character. criticalchance += self.effect_value
            message += f"{character.name}'s crit increase by {self.effect_value}"
            
        # TODO: Add more effect types (speed, critical chance, etc.)
            
        # Remove from inventory after use
        if self in character.inventory:
            character.remove_from_inventory(self)
            
        return message
    
    # TODO: Add method for handling temporary effects that wear off after time
    
    def get_info(self):
        """
        Get detailed information about the consumable.
        
        Returns:
            str: Information about the consumable
        """
        base_info = super().get_info()
        effect_str = f"{self.effect_type.capitalize()} +{self.effect_value}" if self.effect_value >= 0 else f"{self.effect_type.capitalize()} {self.effect_value}"
        return f"{base_info} [Effect: {effect_str}]"
    
    def __eq__(self, other):
        """Check if two consumables are equal."""
        if not isinstance(other, Consumable):
            return False
        return (super().__eq__(other) and 
                self.effect_type == other.effect_type and
                self.effect_value == other.effect_value) 