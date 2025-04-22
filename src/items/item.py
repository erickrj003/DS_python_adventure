# Item Base Class

class Item:
    """
    Base Item class that defines common attributes and behaviors
    for all items in the game.
    """
    
    def __init__(self, name, description, value):
        """
        Initialize a new Item.
        
        Args:
            name (str): The item's name
            description (str): The item's description
            value (int): The item's value in gold coins
        """
        self.name = name
        self.description = description
        self.value = value
    
    def use(self, character):
        """
        Use the item on a character.
        This is a base method to be overridden by subclasses.
        
        Args:
            character: The character using the item
            
        Returns:
            str: A message describing what happened
        """
        return f"{character.name} uses {self.name}, but nothing happens."
    
    def get_info(self):
        """
        Get detailed information about the item.
        
        Returns:
            str: Information about the item
        """
        return f"{self.name} - {self.description} (Value: {self.value} gold)"
    
    def __str__(self):
        """Return string representation of the item."""
        return self.name
    
    def __eq__(self, other):
        """Check if two items are equal."""
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and 
                self.description == other.description and 
                self.value == other.value) 