# NPC class (inherits from Character)

from characters.character import Character

class NPC(Character):
    """
    Non-Player Character class that inherits from Character and adds 
    NPC-specific attributes and behaviors.
    """
    
    def __init__(self, name, health=50, max_health=50, strength=5, defense=5,
                 dialogue=None, is_merchant=False, wares=None):
        """
        Initialize a new NPC.
        
        Args:
            name (str): The NPC's name
            health (int): Current health points
            max_health (int): Maximum health points
            strength (int): NPC's strength (affects damage)
            defense (int): NPC's defense (reduces damage taken)
            dialogue (dict): Dictionary of dialogue options keyed by trigger words
            is_merchant (bool): Whether the NPC is a merchant
            wares (list): Items the merchant sells
        """
        # Call the parent class constructor
        super().__init__(name, health, max_health, strength, defense)
        self.dialogue = dialogue or {}
        self.is_merchant = is_merchant
        self.wares = wares or []
        self.quest = None
        self.friendly = True  # Most NPCs are friendly by default
        self.char_class = "NPC"  # Default class type
        
    def talk(self, keyword=None):
        """
        Get dialogue from the NPC based on a keyword trigger.
        
        Args:
            keyword (str): The keyword to trigger dialogue
            
        Returns:
            str: The NPC's dialogue response
        """
        # Default greeting if no keyword is provided or no match
        if keyword is None or keyword not in self.dialogue:
            if "greeting" in self.dialogue:
                return self.dialogue["greeting"]
            return f"{self.name} nods at you but says nothing."
            
        return self.dialogue[keyword]
    
    def add_dialogue(self, keyword, response):
        """
        Add new dialogue option for the NPC.
        
        Args:
            keyword (str): The keyword to trigger the dialogue
            response (str): The NPC's response
        """
        self.dialogue[keyword] = response
    
    def assign_quest(self, quest):
        """
        Assign a quest to the NPC.
        
        Args:
            quest: The quest object to assign
        """
        self.quest = quest
    
    def get_quest(self):
        """
        Get the NPC's quest.
        
        Returns:
            object: The quest object, or None if no quest
        """
        return self.quest
        
    def add_item_for_sale(self, item, price):
        """
        Add an item to the NPC's wares.
        
        Args:
            item: The item to sell
            price (int): The price of the item
        """
        if not self.is_merchant:
            self.is_merchant = True
        
        self.wares.append({"item": item, "price": price})
    
    def get_wares(self):
        """
        Get the NPC's wares.
        
        Returns:
            list: The items the NPC sells
        """
        if not self.is_merchant:
            return []
        return self.wares
    
    def sell_item(self, index):
        """
        Sell an item from the NPC's wares.
        
        Args:
            index (int): The index of the item to sell
            
        Returns:
            tuple: (item sold, price) or (None, 0) if invalid index
        """
        if not self.is_merchant or index >= len(self.wares):
            return (None, 0)
            
        item_data = self.wares[index]
        return (item_data["item"], item_data["price"])
    
    def __str__(self):
        """Return string representation of the NPC."""
        base_str = super().__str__()
        npc_type = "Merchant" if self.is_merchant else "NPC"
        return f"{base_str} [{npc_type}]" 