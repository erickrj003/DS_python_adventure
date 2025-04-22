# Mr. Johnson's Text-Based RPG Adventure Game
(# TODO: Come up with a better name for our game)

This text-based RPG will serve as our class mini-project to end off our semester in Data Structures during the Spring semester here at Mooseheart. Though the game works in it's current state, it could use several improvements to improve the experience overall. Some of the ideas I've had to improve the game can be seen unofficially as TODO comments. Together, we will emulate a professional software development environment using industry standard tools and practices to make something really cool together!

As a team, your task will include the following:
 - Take ownership of specific TODO tasks and alter the existing code as necessary to fulfill the requirements of that task, following appropriate Object-Oriented Programming principles as necessary
 - Utilize Git to work on the same codebase simultaneously, with the help of Mr. Johnson
 - Come up with your own ideas to improve the big-picture scope of the game

## Project Structure

The project is organized into the following modules:

```
src/
├── characters/          # Character classes
│   ├── character.py     # Base Character class
│   ├── player.py        # Player class (inherits from Character)
│   ├── enemy.py         # Enemy class (inherits from Character)
│   └── npc.py           # NPC class (inherits from Character)
│
├── items/               # Item classes
│   ├── item.py          # Base Item class
│   ├── weapon.py        # Weapon class (inherits from Item)
│   ├── armor.py         # Armor class (inherits from Item)
│   └── consumable.py    # Consumable class (inherits from Item)
│
├── world/               # World and location classes
│   ├── location.py      # Location class
│   └── world.py         # World class to manage locations
│
├── engine/              # Game engine classes
│   ├── game_engine.py   # Main game loop and logic
│   ├── battle_system.py # Combat system
│   └── save_load.py     # Save/load functionality
│
├── ui/                  # User interface
│   └── user_interface.py # Text-based UI
│
├── utils/               # Utility functions
│   └── helpers.py       # Helper functions
│
└── main.py              # Main entry point
```

## Getting Started

1. Make sure you have Python 3.6+ installed
2. Clone or download this project
3. Install dependencies (if/when we add some)
3. Run the game by executing the main.py file:

```
python src/main.py
```

## Project Requirements

This template provides a foundation for what we can currently do in-game:

1. **Character System**
   - Base Character class with attributes like name, health, strength, etc.
   - Derived classes: Player, Enemy, NPC with specialized behaviors
   - Inventory system using composition

2. **Item System**
   - Item base class
   - Specialized subclasses: Weapon, Armor, Consumable
   - Items affect character attributes when equipped or used

3. **Game World**
   - Location class to represent different areas
   - Navigation between locations
   - Descriptions, available actions, and NPCs/enemies for each location

4. **Game Engine**
   - Main game loop that handles player input
   - Battle system using character interactions
   - Save/load feature using file I/O

5. **User Interface**
   - Text-based UI that displays game state
   - Input handling with clear instructions
   - Display of character stats, inventory, location info

## Extension Ideas

Here are some examples of ways to extend this project:

- Add a quest system with objectives and rewards
- Implement a shop/economy system with buying and selling
- Create special abilities for characters
- Add random events that occur while traveling
- Design procedurally generated dungeons or areas
- Add more character classes with unique abilities
- Create a crafting system to make items
- Implement a time system (day/night cycle)
- Add weather effects that impact gameplay

## Object-Oriented Principles Examples

- **Inheritance**: Character subclasses, Item subclasses
- **Encapsulation**: Private methods, getter/setter methods
- **Abstraction**: Starting the game via game.start_game
- **Polymorphism**: Different item types behave differently when used

## Documentation

Most classes and methods are documented with docstrings. Each file includes a file header that explains its purpose and the classes it contains.

## License

This project is provided for educational purposes only.

---