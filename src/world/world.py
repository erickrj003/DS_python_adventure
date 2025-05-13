# World class
import random
from world.location import Location
from characters.enemy import Enemy
from items.weapon import Weapon
from items.armor import Armor
from items.consumable import Consumable

class World:
    """
    World class that manages all locations and the game world state.
    """

    def __init__(self):
        """Initialize a new World."""
        self.locations = {}
        self.starting_location = None
        # TODO: Add weather system that affects gameplay (e.g., rain slows movement, snow reduces visibility)
        self.time_minutes = 0  # Game time in minutes
        self.time_of_day = "Day"  # Can be "Day" or "Night"

    def update_time(self, minutes_passed=10):
         """
        Advance time in the world and update day/night cycle.
        """
        self.time_minutes += minutes_passed
        if (self.time_minutes // 240) % 2 == 0:
            self.time_of_day = "Day"
        else:
            self.time_of_day = "Night"

    def random_event(self):
    # Random Event
        chance = random.randint(100,101)
        if chance >= 1 and chance <= 74: # 75% chance that nothing will happen
            pass
        elif chance >= 75 and chance <= 89: # 15% chance of getting robbed
            self.ui.display_message("You have been robbed!")
            # Player should lose money and items
        else:
            self.ui.display_message("You have been struck by lightning!")
            damage = self.player.take_damage(random.randint(10,20))
            self.ui.display_message(f"You took {damage} damage!")
            # Player should lose health

    def add_location(self, location_id, location):
        self.locations[location_id] = location

    def get_location(self, location_id):
        """
        Get a location by its ID.
        
        Args:
            location_id (str): The ID of the location to get
            
        Returns:
            Location or None: The location with the given ID or None if not found
        """
        self.random_event()
        return self.locations.get(location_id)

    def set_starting_location(self, location_id):
        if location_id in self.locations:
            self.starting_location = self.locations[location_id]
            return True
        return False

    def get_starting_location(self):
        return self.starting_location

    def connect_locations(self, location1_id, direction1, location2_id, direction2=None):
        location1 = self.get_location(location1_id)
        location2 = self.get_location(location2_id)

        if not location1 or not location2:
            return False

        location1.add_connection(direction1, location2)

        if direction2:
            location2.add_connection(direction2, location1)
        else:
            opposites = {
                "north": "south",
                "south": "north",
                "east": "west",
                "west": "east",
                "up": "down",
                "down": "up"
            }
            if direction1 in opposites:
                location2.add_connection(opposites[direction1], location1)

        return True

    def create_world(self):
        town_square = Location("Town Square", "The central square of a small town. People gather here to socialize and trade.")
        blacksmith = Location("Blacksmith", "A hot, smoky forge where the town's blacksmith works on weapons and armor.")
        tavern = Location("Tavern", "A cozy tavern where adventurers gather to share tales and information.")
        forest_path = Location("Forest Path", "A winding path leading into a dark, mysterious forest.")
        forest_clearing = Location("Forest Clearing", "A quiet clearing in the heart of the forest.")
        dark_cave = Location("Dark Cave", "A damp, dark cave with mysterious echoes. It seems dangerous.")

        self.add_location("town_square", town_square)
        self.add_location("blacksmith", blacksmith)
        self.add_location("tavern", tavern)
        self.add_location("forest_path", forest_path)
        self.add_location("forest_clearing", forest_clearing)
        self.add_location("dark_cave", dark_cave)

        self.connect_locations("town_square", "north", "blacksmith")
        self.connect_locations("town_square", "east", "tavern")
        self.connect_locations("town_square", "south", "forest_path")
        self.connect_locations("forest_path", "east", "forest_clearing")
        self.connect_locations("forest_clearing", "north", "dark_cave")

        rusty_sword = Weapon("Rusty Sword", "An old, rusty sword that has seen better days.", 5, 3)
        leather_armor = Armor("Leather Armor", "A simple leather armor that provides basic protection.", 10, 2)
        healing_potion = Consumable("Healing Potion", "A red potion that restores health.", 15, "health", 25)
        strength_potion = Consumable("Strength Potion", "A blue potion that temporarily increases strength.", 20, "strength", 5)
        bow_and_arrow = Weapon("Bow and Arrow", "A bow and arrows dropped from dark skeletons used to shoot from a distance.", 15, 5)
        iron_helmet= Armor("A iron helmet", "a strong helmet used for head protection.,", 15, 4)

        
        # Create enemies and add them to locations
        
        # Forest Path Enemies
        wolf = Enemy("Wolf", health=30, max_health=30, strength=6, defense=2, 
                    level=1, experience_reward=15, 
                    loot_table=[healing_potion])
        forest_path.add_enemy(wolf)

        bandit = Enemy("Bandit", health=45, max_health=45, strength=8, defense=3, 
                       level=2, experience_reward=25, 
                       loot_table=[rusty_sword, healing_potion])
        forest_clearing.add_enemy(bandit)

        bandit_archer = Enemy("Bandit Archer", health=35, max_health=35, strength=10, defense=2, 
                             level=2, experience_reward=30, 
                             loot_table=[healing_potion, strength_potion])
        forest_clearing.add_enemy(bandit_archer)

        cave_spider = Enemy("Giant Spider", health=60, max_health=60, strength=10, defense=3, 
                            level=3, experience_reward=40, 
                            loot_table=[leather_armor, healing_potion, strength_potion])
        dark_cave.add_enemy(cave_spider)

        cave_bat = Enemy("Giant Bat", health=40, max_health=40, strength=7, defense=2, 
                        level=3, experience_reward=35, 
                        loot_table=[healing_potion])
        dark_cave.add_enemy(cave_bat)

        cave_troll = Enemy("Cave Troll", health=100, max_health=100, strength=15, defense=5, 
                          level=5, experience_reward=100, 
                          loot_table=[
                              Weapon("Troll Club", "A massive club that deals heavy damage.", 50, 8),
                              Armor("Troll Hide", "Thick hide that provides strong protection.", 60, 6),
                              healing_potion,
                              healing_potion
                          ])
        dark_cave.add_enemy(cave_troll)

        dark_cave_skeleton = Enemy("Dark cave skeleton", health= 30, max_health= 30, strength= 30, defense= 2, level=5, experience_reward= 75,
                                    loot_table= [
                                        bow_and_arrow, 
                                        healing_potion,
                                        iron_helmet
                                        ])
        dark_cave.add_enemy(dark_cave_skeleton)
        # TODO: Add more enemies with different stats and loot tables
        # TODO: Add NPCs to appropriate locations
        
        # Place items in locations (apart from enemy loot)
        forest_clearing.add_item(healing_potion)

        self.set_starting_location("town_square")

        return self
