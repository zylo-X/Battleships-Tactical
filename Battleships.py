# Battleships Game - Object-Oriented Implementation
import random
import time
import os
from termcolor import colored, cprint
from pyfiglet import figlet_format
import pygame
import sys
import keyboard


class UI:
    """
    Handles all user interface operations including display and input.
    This class isolates the presentation logic from game mechanics.
    """
    def attempt_fullscreen(self):
        """
        Set the terminal to exclusive fullscreen mode using the keyboard library.
        Simulates pressing F11 to trigger fullscreen mode.
        """
        try:
            keyboard.press('f11')
            # Brief pause to allow the fullscreen transition to complete
            import time
            time.sleep(0.5)
            self.clear_screen()  # Clear screen to utilize the new display area
        except Exception as e:
            # Fallback if keyboard library fails
            print("For the best experience, press F11 to enter fullscreen mode.")
            time.sleep(2)
    # ASCII art resources
    SHIP_ART = """ 






                                                         # #  ( )
                                                      ___#_#___|__
                                                  _  |____________|  _
                                           _=====| | |            | | |==== _
                                     =====| |.---------------------------. | |====
                       <--------------------'   .  .  .  .  .  .  .  .   '--------------/
                         \                                                             /
                          \___________________________________________________________/
    """
    
    WATER_ART = """
                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
                    """
    
    LOGO_ART = """
                            █████████████████████████████████████████████████████████
                            █▄─▄─▀██▀▄─██─▄─▄─█─▄─▄─█▄─▄███▄─▄▄─█─▄▄▄▄█─█─█▄─▄█▄─▄▄─█
                            ██─▄─▀██─▀─████─█████─████─██▀██─▄█▀█▄▄▄▄─█─▄─██─███─▄▄▄█
                            ▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▀▀▀
                            """
    
    def __init__(self, sound_manager):
        """Initialize the UI with a sound manager for audio feedback."""
        self.sound_manager = sound_manager
    
    def clear_screen(self):
        """Clear the console screen for a clean display."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def loading_screen(self):
        """
        Display the game's initial loading screen with animated title.
        Creates an engaging first impression for the player.
        """
        print("\n" * 6)  # Create vertical space
        # Display the game title in ASCII art with blinking effect
        cprint(figlet_format('    ZYLO_ X', font='starwars'), 'white', 'on_black', attrs=['blink'])
        cprint(figlet_format('STUDIOS', font='slant'), 'light_green', 'on_black', attrs=['blink'])
        print()
        time.sleep(1.5)   # Pause for 1 second
        self.clear_screen()

    def ship_screen(self):
        """
        Display the ship ASCII art as part of the intro sequence.
        Helps set the nautical theme of the game.
        """
        self.clear_screen()
        cprint(self.LOGO_ART, "red")
        print(self.SHIP_ART)
        cprint(self.WATER_ART, "cyan")
        time.sleep(3)
        self.clear_screen()

    def display_rules(self):
        """
        Display the game rules with retro-style formatting.
        Creates an old-school arcade/computer terminal aesthetic.
        """
        self.clear_screen()
    
        # Title with retro styling
        #cprint(figlet_format("BATTLESHIP", font="banner3-D"), "yellow")
        cprint("                     *** CLASSIFIED NAVAL OPERATIONS MANUAL ***", "red", attrs=["bold"])
    
        # Retro terminal effect
        cprint("\n[SYSTEM INITIALIZED]", "green")
        for _ in range(3):
            cprint(".", "green", end="", flush=True)
            time.sleep(0.3)
        cprint(" LOADING MISSION BRIEFING", "green")
        time.sleep(0.5)
    
        # Top border
        cprint("\n╔════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                          MISSION OBJECTIVES                                ║", "cyan", attrs=["bold"])
        cprint("╠════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║  Sink all enemy vessels before they destroy your fleet.                    ║", "white")
        cprint("╚════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        # Battlefield section
        cprint("\n╔════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                              BATTLEFIELD                                   ║", "cyan", attrs=["bold"])
        cprint("╠════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║  • Two 10x10 grids: YOUR FLEET and ENEMY FLEET                             ║", "white")
        cprint("║  • Your ships are visible; enemy ships remain hidden until hit             ║", "white")
        cprint("║  • Coordinates are entered as ROW (0-9) and COLUMN (0-9)                   ║", "white")
        cprint("╚════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        # Combat section
        cprint("\n╔════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                               COMBAT                                       ║", "cyan", attrs=["bold"])
        cprint("╠════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║  • Players alternate turns, selecting target coordinates                   ║", "white")
        cprint("║  • Hit: 💥  Miss: ⭕  Unexplored: 🟦                                       ║", "white")
        cprint("║  • Once a position is attacked, it cannot be targeted again                ║", "white")
        cprint("║  • Victory is achieved by eliminating all enemy vessels                    ║", "white")
        cprint("╚════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        # Fleet composition
        cprint("\n╔════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                             FLEET COMPOSITION                              ║", "cyan", attrs=["bold"])
        cprint("╠════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║                                                                            ║", "cyan")
        cprint("║      ┌─────────────┬──────────┬───────────────┬────────────────┐           ║", "white")
        cprint("║      │    SHIP     │   SIZE   │    SYMBOL     │     STATUS     │           ║", "white")
        cprint("║      ├─────────────┼──────────┼───────────────┼────────────────┤           ║", "white")
        cprint("║      │  Carrier    │    5     │      🚢       │    ■ ■ ■ ■ ■   │           ║", "white")
        cprint("║      │  Battleship │    4     │      🛥️       │    ■ ■ ■ ■     │           ║", "white")
        cprint("║      │  Cruiser    │    3     │      ⛴️       │    ■ ■ ■       │           ║", "white")
        cprint("║      │  Submarine  │    3     │      ⛵       │    ■ ■ ■       │           ║", "white")
        cprint("║      │  Destroyer  │    2     │      🚤       │    ■ ■         │           ║", "white")
        cprint("║      └─────────────┴──────────┴───────────────┴────────────────┘           ║", "white")
        cprint("║                                                                            ║", "cyan")
        cprint("╚════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        # Final instructions with vintage computer effect
        cprint("\n[TRANSMISSION]", "green")
        time.sleep(0.3)
    
        message = "PLAN YOUR ATTACKS STRATEGICALLY, ADMIRAL. THE FATE OF THE FLEET RESTS IN YOUR HANDS."
        for char in message:
            cprint(char, "green", end="", flush=True)
            time.sleep(0.02)
    
        cprint("\n\n[END OF BRIEFING]", "green")
        cprint("\n[PRESS ENTER TO BEGIN DEPLOYMENT]", "yellow", attrs=["blink"])
    
        input()  # Wait for the player to press Enter
    
    def select_difficulty(self):
        """
        Let the player choose AI difficulty level with detailed explanations.
        Returns: str - "normal" or "hard"
        """
        while True:
            self.clear_screen()
        
            # Stylized header
            cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "cyan")
            cprint("║                           COMBAT DIFFICULTY SELECTION                        ║", "cyan", attrs=["bold"])
            cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "cyan")
            cprint("║  SELECT YOUR ADVERSARY'S TACTICAL CAPABILITIES                               ║", "white")
            cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "cyan")
        
            # Normal difficulty option with explanation
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "green")
            cprint("│ 1. NORMAL DIFFICULTY                                                        │", "green", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "green")
            cprint("│                                                                             │", "green")
            cprint("│  • AI will use random targeting patterns                                    │", "white")
            cprint("│  • Enemy does not prioritize targets based on previous hits                 │", "white")
            cprint("│  • Recommended for casual gameplay or strategic practice                    │", "white")
            cprint("│  • Perfect for new admirals learning naval combat tactics                   │", "white")
            cprint("│                                                                             │", "green")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "green")
        
            # Hard difficulty option with explanation
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "red")
            cprint("│ 2. HARD DIFFICULTY                                                          │", "red", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "red")
            cprint("│                                                                             │", "red")
            cprint("│  • AI employs advanced targeting algorithms                                 │", "white")
            cprint("│  • Enemy will hunt down ships after detecting a hit                         │", "white")
            cprint("│  • Uses probability mapping to predict ship locations                       │", "white")
            cprint("│  • Employs tactical patterns resembling real naval warfare                  │", "white")
            cprint("│  • Recommended for veteran commanders seeking a worthy challege             │", "white")
            cprint("│                                                                             │", "red")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "red")
        
            # Encouraging message
            cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "yellow")
            cprint("║                               ADMIRAL'S WISDOM                               ║", "yellow", attrs=["bold"])
            cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow")
            cprint("║ Remember, victory is determined not just by the challenge you face,          ║", "white")
            cprint("║ but by the strategy you employ and the decisions you make under pressure.    ║", "white")
            cprint("║                                                                              ║", "white")
            cprint("║ Choose the difficulty that will push your tactical skills to their limit,    ║", "white")
            cprint("║ while still providing an engaging and enjoyable naval combat experience.     ║", "white")
            cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "yellow")
        
            # Get player input
            cprint("\n[AWAITING COMMAND] Enter your selection (1 or 2): ", "cyan", attrs=["bold"])
            difficulty = input()
        
            if difficulty == "1":
                self.clear_screen()
                cprint("\n╔══════════════════════════════════════════════════════════════════════╗", "green")
                cprint("║                      NORMAL DIFFICULTY SELECTED                      ║", "green", attrs=["bold"])
                cprint("╚══════════════════════════════════════════════════════════════════════╝", "green")
                cprint("\nPreparing for standard naval operations...", "white")
                cprint("The enemy fleet appears to be using conventional tactics.", "white")
                time.sleep(2)
                return "normal"
            elif difficulty == "2":
                self.clear_screen()
                cprint("\n╔══════════════════════════════════════════════════════════════════════╗", "red")
                cprint("║                       HARD DIFFICULTY SELECTED                       ║", "red", attrs=["bold"])
                cprint("╚══════════════════════════════════════════════════════════════════════╝", "red")
                cprint("\nInitiating advanced combat simulation...", "white")
                cprint("Intelligence reports the enemy commander is highly skilled.", "white")
                cprint("Steel yourself for a challenging engagement, Admiral.", "white")
                time.sleep(2)
                return "hard"
            else:
                cprint("\nInvalid selection. Please enter 1 for Normal or 2 for Hard.", "red")
                time.sleep(1.5)
    def get_placement_choice(self):
        """
        Ask the player how they want to place their ships with detailed explanations.
        Returns: str - "random" or "manual"
        """
        while True:
            self.clear_screen()
        
            # Main header with naval theme
            cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "cyan")
            cprint("║                           FLEET DEPLOYMENT PROTOCOL                          ║", "cyan", attrs=["bold"])
            cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "cyan")
            cprint("║  NAVAL COMMAND REQUIRES YOUR DECISION ON VESSEL POSITIONING                  ║", "white")
            cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "cyan")
        
            # Automatic placement option with pros and cons
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "blue")
            cprint("│ 1. AUTOMATIC DEPLOYMENT (RANDOMIZED POSITIONING)                            │", "blue", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "blue")
            cprint("│                                                                             │", "blue")
            cprint("│  Computer will position your vessels across the grid using randomized       │", "white")
            cprint("│  algorithms derived from chaos theory naval placement strategies.           │", "white")
            cprint("│                                                                             │", "blue")
            cprint("│  ADVANTAGES:                                                                │", "green")
            cprint("│  • Rapid deployment - battle can commence immediately                       │", "white")
            cprint("│  • Unpredictable patterns may confuse enemy targeting systems               │", "white")
            cprint("│  • No risk of clustering vessels in predictable formations                  │", "white")
            cprint("│                                                                             │", "blue")
            cprint("│  DISADVANTAGES:                                                             │", "red")
            cprint("│  • No strategic control over defensive positioning                          │", "white")
            cprint("│  • May place vessels in suboptimal tactical arrangements                    │", "white")
            cprint("│  • Possibility of inadvertent pattern formations detectable by enemy        │", "white")
            cprint("│                                                                             │", "blue")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "blue")
        
            # Manual placement option with pros and cons
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "magenta")
            cprint("│ 2. MANUAL DEPLOYMENT (STRATEGIC POSITIONING)                                │", "magenta", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "magenta")
            cprint("│                                                                             │", "magenta")
            cprint("│  You will personally command the placement of each vessel in your fleet,    │", "white")
            cprint("│  determining exact coordinates and orientation for maximum tactical effect. │", "white")
            cprint("│                                                                             │", "magenta")
            cprint("│  ADVANTAGES:                                                                │", "green")
            cprint("│  • Complete strategic control over defensive posture                        │", "white")
            cprint("│  • Ability to implement proven naval formation tactics                      │", "white")
            cprint("│  • Can adapt positioning based on anticipated enemy behavior                │", "white")
            cprint("│  • Potential to create deliberate deception patterns                        │", "white")
            cprint("│                                                                             │", "magenta")
            cprint("│  DISADVANTAGES:                                                             │", "red")
            cprint("│  • More time required for battle preparation                                │", "white")
            cprint("│  • Human patterns may be more predictable to advanced AI                    │", "white")
            cprint("│  • Risk of tactical errors in vessel placement                              │", "white")
            cprint("│                                                                             │", "magenta")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "magenta")
        

            # Input prompt
            cprint("\n[AWAITING COMMAND] Enter deployment protocol (1 or 2): ", "cyan", attrs=["bold"])
            choice = input().strip()
        
            if choice == "1":
                self.clear_screen()
                cprint("\n╔══════════════════════════════════════════════════════════════════════╗", "blue")
                cprint("║                    AUTOMATIC DEPLOYMENT SELECTED                     ║", "blue", attrs=["bold"])
                cprint("╚══════════════════════════════════════════════════════════════════════╝", "blue")
                cprint("\nComputer algorithms positioning fleet...", "white")
                cprint("Randomizing vessel coordinates for optimal unpredictability...", "white")
                time.sleep(1.5)
                return "random"
            elif choice == "2":
                self.clear_screen()
                cprint("\n╔══════════════════════════════════════════════════════════════════════╗", "magenta")
                cprint("║                     MANUAL DEPLOYMENT SELECTED                       ║", "magenta", attrs=["bold"])
                cprint("╚══════════════════════════════════════════════════════════════════════╝", "magenta")
                cprint("\nInitializing tactical grid interface...", "white")
                cprint("Prepare to position your vessels, Admiral.", "white")
                time.sleep(1.5)
                return "manual"
            else:
                cprint("\nInvalid selection. Please enter 1 for Automatic or 2 for Manual Deployment.", "red")
                time.sleep(1.5)
    
    def display_manual_placement_instructions(self):
        """Display instructions for manual ship placement."""
        self.clear_screen()
        cprint("\n╔════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                       MANUAL DEPLOYMENT PROTOCOL                           ║", "cyan", attrs=["bold"])
        cprint("╠════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║ Instructions:                                                              ║", "white")
        cprint("║  • You will place each of your 5 ships on the grid one by one              ║", "white")
        cprint("║  • For each ship, enter the starting coordinates (row, column)             ║", "white")
        cprint("║  • Then choose orientation (horizontal or vertical)                        ║", "white")
        cprint("║  • Ships cannot overlap or extend beyond the grid boundaries               ║", "white")
        cprint("║                                                                            ║", "white")
        cprint("║ Remember, strategic positioning is critical for naval victory!             ║", "white")
        cprint("╚════════════════════════════════════════════════════════════════════════════╝", "cyan")
        cprint("\n[PRESS ENTER TO BEGIN DEPLOYMENT]", "yellow", attrs=["blink"])
        input()

    def display_ship_placement_board(self, board, ship_name, ship_size):
        """
        Display the board during manual ship placement.
        
        Args:
            board (Board): The player's board
            ship_name (str): Name of the ship being placed
            ship_size (int): Size of the ship being placed
        """
        self.clear_screen()
        
        # Display current board
        cprint("\n╔══════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                   FLEET DEPLOYMENT INTERFACE                 ║", "cyan", attrs=["bold"])
        cprint("╚══════════════════════════════════════════════════════════════╝", "cyan")
        
        # Column headers
        cprint("    " + "  ".join(f"{i}" for i in range(10)), "yellow")
        
        # Grid border
        cprint("  ┌" + "─" * 31 + "┐", "cyan")
        
        # Print rows
        for idx, row in enumerate(board.visible_grid):
            formatted_row = " ".join(self._format_cell(cell) for cell in row)
            cprint(f"{idx} │ {formatted_row} │", "cyan")
        
        # Bottom grid border
        cprint("  └" + "─" * 31 + "┘", "cyan")
        
        # Special case for "All ships" display
        if ship_name == "All ships":
            cprint(f"\nFleet deployment complete!", "green", attrs=["bold"])
            cprint(f"All ships have been positioned on the grid.", "yellow")
        else:
            # Display ship information for normal placement
            cprint(f"\nCurrently placing: {ship_name} (Size: {ship_size})", "green", attrs=["bold"])
            emoji = Ship.SHIP_EMOJIS[ship_name]
            cprint(f"Ship symbol: {emoji}", "yellow")
    
    def _format_cell(self, cell):
        """Format a single cell for display during ship placement."""
        if cell == "X":  # Hit
            return colored("💥", "red", attrs=["bold"])
        elif cell == "O":  # Miss
            return colored("⭕", "white")
        elif cell in Ship.SHIP_EMOJIS.values():  # Ship
            return colored(cell, "yellow")
        else:  # Water
            return colored("🟦", "blue")
    
    def get_ship_placement_coordinates(self, ship_name, ship_size):
        """
        Get coordinates and orientation for ship placement.
        
        Args:
            ship_name (str): Name of the ship being placed
            ship_size (int): Size of the ship
            
        Returns:
            tuple: (row, col, orientation) where orientation is "horizontal" or "vertical"
        """
        # Input row
        while True:
            try:
                cprint(f"Enter starting ROW for {ship_name} (0-9): ", "cyan")
                row_input = input().strip()
                if row_input.isdigit() and 0 <= int(row_input) < 10:
                    row = int(row_input)
                    break
                else:
                    cprint("Invalid input. Please enter a number between 0 and 9.", "red")
            except:
                cprint("Invalid input. Please enter a number between 0 and 9.", "red")
        
        # Input column
        while True:
            try:
                cprint(f"Enter starting COLUMN for {ship_name} (0-9): ", "cyan")
                col_input = input().strip()
                if col_input.isdigit() and 0 <= int(col_input) < 10:
                    col = int(col_input)
                    break
                else:
                    cprint("Invalid input. Please enter a number between 0 and 9.", "red")
            except:
                cprint("Invalid input. Please enter a number between 0 and 9.", "red")
        
        # Input orientation
        while True:
            cprint("Enter orientation (H for horizontal, V for vertical): ", "cyan")
            orientation_input = input().strip().upper()
            if orientation_input == "H":
                orientation = "horizontal"
                break
            elif orientation_input == "V":
                orientation = "vertical"
                break
            else:
                cprint("Invalid input. Please enter H or V.", "red")
        
        return row, col, orientation
        
    def display_boards(self, player_board, cpu_board, cpu_ship_parts=None):
        """
        Display both player and CPU boards in retro command console style.
        Creates an immersive naval battle station aesthetic.
    
        Args:
            player_board (Board): The player's board object
            cpu_board (Board): The CPU's board object
            cpu_ship_parts (dict): Optional tracking of CPU ship parts for display
        """
        self.clear_screen()
    
        # Command console header
        cprint("╔══════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                          NAVAL COMMAND INTERFACE                             ║", "cyan")
        cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        def format_cell(cell):
            """Render cells with military-style indicators."""
            if cell == "X":  # Hit
                return colored("💥", "red", attrs=["bold"])
            elif cell == "O":  # Miss
                return colored("⭕", "white")
            elif cell in Ship.SHIP_EMOJIS.values():  # Ship (only visible on player's board)
                return colored(cell, "yellow")
            else:  # Water
                return colored("🟦", "blue")
    
        # Get the grid representations
        player_grid = player_board.visible_grid
        cpu_grid = cpu_board.visible_grid
    
        # Calculate battle statistics
        player_hits = sum(row.count("X") for row in cpu_grid)
        player_misses = sum(row.count("O") for row in cpu_grid)
        player_accuracy = player_hits / (player_hits + player_misses) * 100 if (player_hits + player_misses) > 0 else 0
    
        cpu_hits = sum(row.count("X") for row in player_grid)
        cpu_misses = sum(row.count("O") for row in player_grid)
        cpu_accuracy = cpu_hits / (cpu_hits + cpu_misses) * 100 if (cpu_hits + cpu_misses) > 0 else 0
    
        # Battle grids header
        cprint("\n╔═════════════════════════════════╗", "green", end="")
        cprint("          ╔═════════════════════════════════╗", "red")
        cprint("║       FRIENDLY WATERS           ║", "green", end="")
        cprint("          ║        ENEMY WATERS             ║", "red")
        cprint("╚═════════════════════════════════╝", "green", end="")
        cprint("          ╚═════════════════════════════════╝", "red")
    
        # Column headers
        cprint("    " + "  ".join(f"{i}" for i in range(10)), "yellow", end="")
        cprint("                 " + "  ".join(f"{i}" for i in range(10)), "yellow")
    
        # Grid borders
        cprint(" ┌" + "─" * 31 + "┐", "cyan", end="")
        cprint("            ┌" + "─" * 31 + "┐", "cyan")
    
        # Print rows with radar-style formatting
        for idx in range(10):
            player_row = " ".join(format_cell(cell) for cell in player_grid[idx])
            cpu_row = " ".join(format_cell(cell) for cell in cpu_grid[idx])
        
            cprint(f"{idx}│", "yellow", end=" ")
            cprint(f"{player_row}", end=" ")
            cprint("│", "cyan", end="")
            cprint("           ", end="")
            cprint(f"{idx}│", "yellow", end=" ")
            cprint(f"{cpu_row}", end=" ")
            cprint("│", "cyan")
    
        # Bottom grid borders
        cprint(" └" + "─" * 31 + "┘", "cyan", end="")
        cprint("            └" + "─" * 31 + "┘", "cyan")
    
        # Battle status display
        cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "yellow")
        cprint("║                             TACTICAL READOUT                                 ║", "yellow")
        cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow")
    
        # Combat indicators
        cprint("║  RADAR SYMBOLS:  ", "white", end="")
        cprint("💥 ", "red", end="")
        cprint("= CONFIRMED HIT    ", "white", end="")
        cprint("⭕ ", "white", end="")
        cprint("= MISS    ", "white", end="")
        cprint("🟦 ", "blue", end="")
        cprint("= UNSCANNED WATERS    ║", "white")
    
        # Combat statistics - FIXED VERSION
        cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow")
    
        # Fix 1: Properly format the player statistics line
        padding = " " * (24 - len(f"{player_accuracy:.1f}"))
        player_stats = f"║  YOUR STATISTICS: Hits: {player_hits} | Misses: {player_misses} | Accuracy: {player_accuracy:.1f}%{padding}  ║"
        cprint(player_stats, "white")
    
        # Fix 2: Properly format the enemy statistics line
        padding = " " * (23 - len(f"{cpu_accuracy:.1f}"))
        enemy_stats = f"║  ENEMY STATISTICS: Hits: {cpu_hits} | Misses: {cpu_misses} | Accuracy: {cpu_accuracy:.1f}%{padding}  ║"
        cprint(enemy_stats, "white")
    
        # Remaining enemy fleet status
        if cpu_ship_parts:
            cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow")
            cprint("║                           ENEMY FLEET STATUS                                 ║", "yellow")
        
            # Initialize status indicators
            status_indicators = []
        
            for ship_name, positions in cpu_ship_parts.items():
                emoji = Ship.SHIP_EMOJIS[ship_name]
                total = Ship.SHIP_SIZES[ship_name]
                remaining = len(positions)
                hits = total - remaining
            
                # Create a visual health bar    
                health_bar = "█" * remaining + "░" * hits
            
                if remaining == 0:
                    status = colored("DESTROYED", "red", attrs=["bold"])
                elif hits > 0:
                    status = colored("DAMAGED", "yellow", attrs=["bold"])
                else:
                    status = colored("OPERATIONAL", "green", attrs=["bold"]) 
            
                # Format: Ship emoji, name, health bar, status
                ship_status = f"║  {emoji} {ship_name.ljust(10)} {health_bar.ljust(6)} {status.ljust(68)}║"
                status_indicators.append(ship_status)
        
            # Print all ship statuses
            for indicator in status_indicators:
                cprint(indicator, "white")
    
        cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "yellow")
    
        # Show a retro-style prompt
        cprint("\n[SELECT TARGET COORDINATES]", "green", attrs=["bold"])
    
    def get_attack_coordinates(self):
        """
        Get attack coordinates from the player.
        
        Returns:
            tuple: (row, col) coordinates for attack
        """
        # Input row from player
        while True:
            try:
                cprint("Enter a Row number from the grid (0 to 9): ", "cyan")
                row_input = input()
                if row_input.isdigit() and 0 <= int(row_input) < 10:
                    row = int(row_input)
                    break
                else:
                    cprint("Invalid input. Please select a valid row between 0 and 9.", "red")
                    time.sleep(0.5)
            except:
                cprint("Invalid input. Please select a valid row between 0 and 9.", "red")
                time.sleep(0.5)

        # Input column from player
        while True:
            try:
                cprint("Enter a Column number from the grid (0 to 9): ", "cyan")
                col_input = input()
                if col_input.isdigit() and 0 <= int(col_input) < 10:
                    col = int(col_input)
                    break
                else:
                    cprint("Invalid input. Please select a valid column between 0 and 9.", "red")
                    time.sleep(0.5)
            except:
                cprint("Invalid input. Please select a valid column between 0 and 9.", "red")
                time.sleep(0.5)
        return row, col
    
    def ask_play_again(self):
        """
        Ask the player if they want to play again.
        
        Returns:
            bool: True if player wants to play again, False otherwise
        """
        cprint("Do you want to play again? (Y/N): ", "cyan", attrs=["bold"])
        answer = input().strip().lower()
        return answer in ["y", "yes"]


class SoundManager:
    """
    Manages all game sounds and sound effects.
    Centralizes audio handling for consistent sound experience.
    """
    def __init__(self):
        """Initialize pygame mixer and load all game sounds from Assets folder."""
        import os
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Define the assets folder path
        if getattr(sys, 'frozen', False):
            # Running in a PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # Running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))

        assets_folder = os.path.join(base_path, "Assets")

        
        # Function to load a sound file with error handling
        def load_sound(filename):
            filepath = os.path.join(assets_folder, filename)
            try:
                return pygame.mixer.Sound(filepath)
            except pygame.error as e:
                print(f"Warning: Could not load sound file {filepath}")
                print(f"Error details: {e}")
                # Return a dummy sound object that does nothing to prevent crashes
                class DummySound:
                    def play(self): pass
                    def stop(self): pass
                return DummySound()
        
        # Load all sounds
        self.intro_sound = load_sound("intro.mp3")
        self.hit_sound = load_sound("Hit.mp3")
        self.miss_sound = load_sound("miss.mp3")
        self.win_sound = load_sound("win.mp3")
        self.gameover_sound = load_sound("gameover.mp3")
        self.place_ship_sound = load_sound("miss.mp3")  # New sound for ship placement
    
    def play_intro(self):
        """Play the introduction sound."""
        self.intro_sound.play()
    
    def stop_intro(self):
        """Stop the introduction sound."""
        self.intro_sound.stop()
    
    def play_hit(self):
        """Play the hit sound effect."""
        self.hit_sound.play()
    
    def play_miss(self):
        """Play the miss sound effect."""
        self.miss_sound.play()
    
    def play_win(self):
        """Play the winning sound."""
        self.win_sound.play()
    
    def play_gameover(self):
        """Play the game over sound."""
        self.gameover_sound.play()
        
    def play_place_ship(self):
        """Play the ship placement sound."""
        self.place_ship_sound.play()


class Ship:
    """
    Represents a ship in the game with its attributes and state.
    Tracks ship position and damage.
    """
    # Ship size dictionary
    SHIP_SIZES = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2
    }
    
    # Ship emoji mapping
    SHIP_EMOJIS = {
        "Carrier": "🚢",
        "Battleship": "🛥️",
        "Cruiser": "⛴️",
        "Submarine": "⛵",
        "Destroyer": "🚤"
    }
    
    def __init__(self, name):
        """
        Initialize a ship with its name and corresponding attributes.
        
        Args:
            name (str): The name of the ship (e.g., "Carrier")
        """
        self.name = name
        self.size = self.SHIP_SIZES[name]
        self.emoji = self.SHIP_EMOJIS[name]
        self.positions = set()  # Will store (row, col) tuples
        
    def is_sunk(self):
        """
        Check if the ship is sunk (no positions left).
        
        Returns:
            bool: True if the ship is sunk, False otherwise
        """
        return len(self.positions) == 0
    
    def register_hit(self, row, col):
        """
        Register a hit on the ship by removing the position.
        
        Args:
            row (int): Row coordinate of the hit
            col (int): Column coordinate of the hit
            
        Returns:
            bool: True if the hit was successful (position existed), False otherwise
        """
        if (row, col) in self.positions:
            self.positions.remove((row, col))
            return True
        return False


class Board:
    """
    Represents a game board with ship placement and attack tracking.
    Manages the state of a player's grid.
    """
    def __init__(self, is_player=True):
        """
        Initialize a board with empty grids.
        
        Args:
            is_player (bool): Whether this is the player's board (True) or CPU's (False)
        """
        self.is_player = is_player
        self.hidden_grid = [["~" for _ in range(10)] for _ in range(10)]
        self.visible_grid = [["~" for _ in range(10)] for _ in range(10)]
        self.ships = {}  # Will store Ship objects
        
        # Initialize ships
        for ship_name in Ship.SHIP_SIZES:
            self.ships[ship_name] = Ship(ship_name)
    
    def place_ships_randomly(self):
        """
        Place all ships randomly on the board.
        Updates both the grid and each ship's positions.
        """
        for ship_name, ship in self.ships.items():
            self._place_single_ship(ship)
            
    def place_ships_manually(self, ui, sound_manager):
        """
        Place all ships manually with user input.
        
        Args:
            ui (UI): The UI object for interaction
            sound_manager (SoundManager): Sound manager for audio feedback
            
        Returns:
            bool: True if all ships were placed successfully
        """
        # Display instructions for manual placement
        ui.display_manual_placement_instructions()
        
        # Place each ship one by one
        ship_placement_order = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        
        for ship_name in ship_placement_order:
            ship = self.ships[ship_name]
            placed = False
            
            while not placed:
                # Display the current board state and ship info
                ui.display_ship_placement_board(self, ship_name, ship.size)
                
                # Get placement coordinates and orientation
                row, col, orientation = ui.get_ship_placement_coordinates(ship_name, ship.size)
                
                # Try to place the ship
                if self._place_single_ship_manually(ship, row, col, orientation):
                    # Ship placed successfully
                    placed = True
                    sound_manager.play_place_ship()
                    cprint(f"{ship_name} placed successfully!", "green", attrs=["bold"])
                    time.sleep(0.5)
                else:
                    # Invalid placement
                    cprint("Invalid placement! Ship would overlap or extend beyond grid boundaries.", "red", attrs=["bold"])
                    time.sleep(0.5)
        
        # Show the final fleet deployment
        ui.display_ship_placement_board(self, "All ships", 0)
        cprint("\nFleet deployment complete!", "green", attrs=["bold"])
        cprint("Your ships are positioned and ready for battle.", "green")
        cprint("\n[PRESS ENTER TO BEGIN COMBAT]", "yellow", attrs=["blink"])
        input()
        
        return True
    
    def _place_single_ship(self, ship):
        """
        Place a single ship randomly on the board.
        
        Args:
            ship (Ship): The ship object to place
        """
        ship_length = ship.size
        ship_emoji = ship.emoji
        
        # Keep trying until a valid placement is found
        while True:
            direction = random.choice(["horizontal", "vertical"])
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            
            # Check if placement is valid
            if direction == "horizontal":
                if col + ship_length > 10:
                    continue
                if any(self.hidden_grid[row][c] != "~" for c in range(col, col + ship_length)):
                    continue
                
                # Place the ship
                for c in range(col, col + ship_length):
                    self.hidden_grid[row][c] = ship_emoji
                    if self.is_player:
                        self.visible_grid[row][c] = ship_emoji
                    ship.positions.add((row, c))
                break
                
            elif direction == "vertical":
                if row + ship_length > 10:
                    continue
                if any(self.hidden_grid[r][col] != "~" for r in range(row, row + ship_length)):
                    continue
                
                # Place the ship
                for r in range(row, row + ship_length):
                    self.hidden_grid[r][col] = ship_emoji
                    if self.is_player:
                        self.visible_grid[r][col] = ship_emoji
                    ship.positions.add((r, col))
                break
    
    def _place_single_ship_manually(self, ship, row, col, orientation):
        """
        Place a single ship manually on the board.
        
        Args:
            ship (Ship): The ship object to place
            row (int): Starting row coordinate
            col (int): Starting column coordinate
            orientation (str): "horizontal" or "vertical"
            
        Returns:
            bool: True if placement was successful, False if invalid
        """
        ship_length = ship.size
        ship_emoji = ship.emoji
        
        # Check if placement is valid
        if orientation == "horizontal":
            # Check boundaries
            if col + ship_length > 10:
                return False
            
            # Check for overlaps
            if any(self.hidden_grid[row][c] != "~" for c in range(col, col + ship_length)):
                return False
            
            # Place the ship
            for c in range(col, col + ship_length):
                self.hidden_grid[row][c] = ship_emoji
                if self.is_player:
                    self.visible_grid[row][c] = ship_emoji
                ship.positions.add((row, c))
                
        elif orientation == "vertical":
            # Check boundaries
            if row + ship_length > 10:
                return False
            
            # Check for overlaps
            if any(self.hidden_grid[r][col] != "~" for r in range(row, row + ship_length)):
                return False
            
            # Place the ship
            for r in range(row, row + ship_length):
                self.hidden_grid[r][col] = ship_emoji
                if self.is_player:
                    self.visible_grid[r][col] = ship_emoji
                ship.positions.add((r, col))
        
        return True
    
    def register_attack(self, row, col, sound_manager):
        """
        Register an attack on the board.
        
        Args:
            row (int): Row coordinate of the attack
            col (int): Column coordinate of the attack
            sound_manager (SoundManager): Sound manager for audio feedback
            
        Returns:
            tuple: (result message, hit_ship) where hit_ship is the ship that was hit or None
        """
        # Check if the cell has already been attacked
        if self.visible_grid[row][col] in ["X", "O"]:
            return (colored("Already guessed!", "yellow"), None)
        
        # Check if there's a ship at the position
        if self.hidden_grid[row][col] in Ship.SHIP_EMOJIS.values():
            # Find which ship was hit
            hit_ship = None
            for ship in self.ships.values():
                if (row, col) in ship.positions:
                    hit_ship = ship
                    break
            
            if hit_ship:
                # Register the hit
                hit_ship.register_hit(row, col)
                
                # Update grids
                self.hidden_grid[row][col] = "X"
                self.visible_grid[row][col] = "X"
                
                # Play sound
                sound_manager.play_hit()
                
                # Check if ship is sunk
                if hit_ship.is_sunk():
                    return (colored(f"{hit_ship.name} has been destroyed!", "magenta", attrs=["bold"]), hit_ship)
                else:
                    return (colored(f"Hit on {hit_ship.name}!", "green", attrs=["bold"]), hit_ship)
        
        # Otherwise it's a miss
        if self.hidden_grid[row][col] == "~":
            self.visible_grid[row][col] = "O"
            sound_manager.play_miss()
            return (colored("Miss!", "red", attrs=["bold"]), None)
        
        return (colored("Invalid attack!", "red"), None)
    
    def all_ships_sunk(self):
        """
        Check if all ships on the board have been sunk.
        
        Returns:
            bool: True if all ships are sunk, False otherwise
        """
        return all(ship.is_sunk() for ship in self.ships.values())


class Player:
    """
    Base class for game players (human and AI).
    Defines common player functionality.
    """
    def __init__(self, name, is_human=True):
        """
        Initialize a player with a name and board.
        
        Args:
            name (str): Player name
            is_human (bool): Whether this is a human player
        """
        self.name = name
        self.is_human = is_human  # Store is_human as an attribute
        self.board = Board(is_player=is_human)
        
    def setup(self, placement_method="random", ui=None, sound_manager=None):
        """
        Set up the player's board by placing ships.
    
        Args:
            placement_method (str): "random" or "manual"
            ui (UI): UI object for interaction
            sound_manager (SoundManager): Sound manager for audio feedback
        
        Returns:
            bool: True if setup was successful
        """
        if placement_method == "random" or not self.is_human:  # FIXED: Using self.is_human
            self.board.place_ships_randomly()
        else:
            self.board.place_ships_manually(ui, sound_manager)
        return True


class AIPlayer(Player):
    """
    Computer player with different difficulty levels.
    Implements AI attack strategies.
    """
    def __init__(self, difficulty="normal"):
        """
        Initialize an AI player with specified difficulty.
        
        Args:
            difficulty (str): The AI difficulty - "normal" or "hard"
        """
        super().__init__("CPU", is_human=False)
        self.difficulty = difficulty
        
        # For tracking AI attack strategy
        self.hits = []
        self.potential_targets = []
        self.probability_map = [[1 for _ in range(10)] for _ in range(10)]
    
    def attack(self, opponent_board, sound_manager):
        """
        Execute an AI attack based on difficulty level.
        
        Args:
            opponent_board (Board): The opponent's board to attack
            sound_manager (SoundManager): Sound manager for audio feedback
            
        Returns:
            tuple: (attack result message, attack coordinates)
        """
        if self.difficulty == "normal":
            return self._normal_attack(opponent_board, sound_manager)
        else:
            return self._hard_attack(opponent_board, sound_manager)
    
    def _normal_attack(self, opponent_board, sound_manager):
        """
        Execute a random attack strategy.
        
        Args:
            opponent_board (Board): The opponent's board to attack
            sound_manager (SoundManager): Sound manager for audio feedback
            
        Returns:
            tuple: (attack result message, attack coordinates)
        """
        # Choose random coordinates until finding an unattacked cell
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if opponent_board.visible_grid[row][col] not in ["X", "O"]:
                break
        
        # Announce and execute the attack
        cprint(f"AI attacks at ({row}, {col})", "magenta", attrs=["bold"])
        result, hit_ship = opponent_board.register_attack(row, col, sound_manager)
        
        return result, (row, col)
    
    def _hard_attack(self, opponent_board, sound_manager):
        """
        Execute an intelligent attack strategy that targets ships.
        
        Args:
            opponent_board (Board): The opponent's board to attack
            sound_manager (SoundManager): Sound manager for audio feedback
            
        Returns:
            tuple: (attack result message, attack coordinates)
        """
        # Print debug info
        #print(f"DEBUG: Hard AI is thinking...")
        #print(f"DEBUG: Current hits: {self.hits}")
        #print(f"DEBUG: Potential targets: {self.potential_targets}")
        
        # Choose attack coordinates
        row, col = None, None
        
        # If we have potential targets, use them
        if self.potential_targets:
            # Use the highest priority target
            row, col = self.potential_targets.pop(0)
            #print(f"DEBUG: Using potential target: ({row}, {col})")
        
        # If we have hits but no targets, analyze ship direction
        elif self.hits and not self.potential_targets:
            #print("DEBUG: Analyzing ship direction...")
            self._analyze_ship_direction(opponent_board)
            
            if self.potential_targets:
                row, col = self.potential_targets.pop(0)
                #print(f"DEBUG: Using direction-based target: ({row}, {col})")
            else:
                # Fall back to probability-based targeting
                row, col = self._probability_based_attack(opponent_board)
        
        # Otherwise use probability-based targeting
        else:
            #print("DEBUG: Using probability-based targeting")
            row, col = self._probability_based_attack(opponent_board)
        
        # Announce and execute the attack
        cprint(f"AI attacks at ({row}, {col})", "magenta", attrs=["bold"])
        result, hit_ship = opponent_board.register_attack(row, col, sound_manager)
        result_text = str(result)
        
        # Update AI tracking based on result
        if ("Hit" in result_text or "destroyed" in result_text) and "Already" not in result_text:
            #print(f"DEBUG: Hit confirmed at ({row}, {col})")
            self.hits.append((row, col))
            
            # Add adjacent cells as potential targets
            self._update_potential_targets(row, col, opponent_board)
            
            # If a ship was completely destroyed, clear related targets
            if hit_ship and hit_ship.is_sunk():
                self._clear_sunk_ship_targets()
        else:
            # Update probability map for misses
            if opponent_board.visible_grid[row][col] == "O":
                self._update_probability_map(row, col, -1)
        
        #print(f"DEBUG: After attack - Hits: {self.hits}, Targets: {self.potential_targets}")
        return result, (row, col)
    
    def _analyze_ship_direction(self, opponent_board):
        """
        Analyze hit patterns to determine ship direction.
        Updates potential targets based on alignment.
        
        Args:
            opponent_board (Board): The opponent's board
        """
        if len(self.hits) >= 2:
            # Check if hits are aligned horizontally or vertically
            rows = [hit[0] for hit in self.hits]
            cols = [hit[1] for hit in self.hits]
            
            if len(set(rows)) == 1:  # Horizontal alignment
                row = rows[0]
                min_col = min(cols)
                max_col = max(cols)
                
                # Try left side
                if min_col > 0 and opponent_board.visible_grid[row][min_col-1] not in ["X", "O"]:
                    self.potential_targets.insert(0, (row, min_col-1))
                
                # Try right side
                if max_col < 9 and opponent_board.visible_grid[row][max_col+1] not in ["X", "O"]:
                    self.potential_targets.insert(0, (row, max_col+1))
            
            elif len(set(cols)) == 1:  # Vertical alignment
                col = cols[0]
                min_row = min(rows)
                max_row = max(rows)
                
                # Try top
                if min_row > 0 and opponent_board.visible_grid[min_row-1][col] not in ["X", "O"]:
                    self.potential_targets.insert(0, (min_row-1, col))
                
                # Try bottom
                if max_row < 9 and opponent_board.visible_grid[max_row+1][col] not in ["X", "O"]:
                    self.potential_targets.insert(0, (max_row+1, col))
    
    def _update_potential_targets(self, row, col, opponent_board):
        """
        Add adjacent cells to potential targets after a hit.
        
        Args:
            row (int): Row of the hit
            col (int): Column of the hit
            opponent_board (Board): The opponent's board
        """
        # Check cells in four directions (up, right, down, left)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (0 <= nr < 10 and 0 <= nc < 10 and 
                opponent_board.visible_grid[nr][nc] not in ["X", "O"] and
                (nr, nc) not in self.potential_targets):
                self.potential_targets.append((nr, nc))
    
    def _clear_sunk_ship_targets(self):
        """
        Clear targeting data after sinking a ship.
        Resets AI strategy for finding the next ship.
        """
        self.hits = []
        # Keep other potential targets but prioritize differently
        self.potential_targets = [target for target in self.potential_targets 
                                 if not any(abs(target[0]-h[0]) + abs(target[1]-h[1]) <= 1 
                                           for h in self.hits)]
    
    def _probability_based_attack(self, opponent_board):
        """
        Choose a target based on probability density.
        Higher probability cells are more likely to contain ships.
        
        Args:
            opponent_board (Board): The opponent's board
            
        Returns:
            tuple: (row, col) coordinates for attack
        """
        # Find valid cells (not already attacked)
        valid_cells = []
        for r in range(10):
            for c in range(10):
                if opponent_board.visible_grid[r][c] not in ["X", "O"]:
                    valid_cells.append((r, c, self.probability_map[r][c]))
        
        # If using checkerboard pattern for efficiency
        if not self.hits:
            # Prioritize cells with even parity (checkerboard pattern)
            parity_cells = [(r, c, prob*1.5) for r, c, prob in valid_cells if (r + c) % 2 == 0]
            if parity_cells:
                valid_cells = parity_cells
        
        # Select cell based on probability weighting
        if valid_cells:
            total_prob = sum(prob for _, _, prob in valid_cells)
            target_value = random.uniform(0, total_prob)
            cumulative = 0
            
            for r, c, prob in valid_cells:
                cumulative += prob
                if cumulative >= target_value:
                    return r, c
        
        # Fallback to random selection if no valid cells (shouldn't happen)
        return random.randint(0, 9), random.randint(0, 9)
    
    def _update_probability_map(self, row, col, change):
        """
        Update the probability map based on attack results.
        
        Args:
            row (int): Row of the attack
            col (int): Column of the attack
            change (int): Value to add to probability (negative for miss)
        """
        # Update the targeted cell
        self.probability_map[row][col] = max(0, self.probability_map[row][col] + change)
        
        # For misses, also reduce probability in adjacent cells
        if change < 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        self.probability_map[nr][nc] = max(0, self.probability_map[nr][nc] + change//2)
    
    def reset(self):
        """Reset AI tracking data for a new game."""
        self.hits = []
        self.potential_targets = []
        self.probability_map = [[1 for _ in range(10)] for _ in range(10)]



class BattleshipGame:
    """
    Main game controller class that manages the overall game flow.
    Coordinates all components and handles the game loop.
    """
    def __init__(self):
        """Initialize the game with necessary components."""

        self.sound_manager = SoundManager()
        self.ui = UI(self.sound_manager)
        self.player = None
        self.ai = None
    
    def initialize_game(self):
        """Set up a new game by initializing players and boards."""
        # Create the human player
        self.player = Player("Player")
        
        # Show intro screens and play sound
        self.ui.attempt_fullscreen()    
        self.ui.loading_screen()
        self.ui.ship_screen()
        self.sound_manager.play_intro()
        
        # Display rules and get difficulty
        self.ui.display_rules()
        difficulty = self.ui.select_difficulty()
        
        # Create AI with selected difficulty
        self.ai = AIPlayer(difficulty)
        
        # Ask how player wants to place ships
        placement_method = self.ui.get_placement_choice()
        
        # Set up boards
        self.ai.setup()  # AI always uses random placement
        self.player.setup(placement_method, self.ui, self.sound_manager)
        
        # Stop intro sound
        self.sound_manager.stop_intro()
        self.ui.clear_screen()
    
    def play_game(self):
        """
        Main game loop that manages player and AI turns.
        Continues until a win condition is met.
        """
        game_over = False
        
        while not game_over:
            # Player's turn
            self._player_turn()
            
            # Check if player won
            if  self.ai.board.all_ships_sunk():
                self._handle_player_win()
                game_over = True
                continue
            
            # AI's turn
            self._ai_turn()
            
            # Check if AI won
            if self.player.board.all_ships_sunk():
                self._handle_ai_win()
                game_over = True
    
    def _player_turn(self):
        """Handle the player's turn including attack and result display."""
        valid_attack = False
        
        while not valid_attack:
            # Display boards
            self.ui.clear_screen()
            cpu_ship_parts = {name: ship.positions for name, ship in self.ai.board.ships.items()}
            self.ui.display_boards(self.player.board, self.ai.board, cpu_ship_parts)
            
            # Get attack coordinates
            row, col = self.ui.get_attack_coordinates()
            
            # Process attack
            result, _ = self.ai.board.register_attack(row, col, self.sound_manager)
            cprint(result, "green" if "Hit" in str(result) else "red")
            
            # Check if attack was valid
            if "Already guessed!" not in str(result):
                valid_attack = True
            else:
                time.sleep(0.5)
                self.ui.clear_screen()
        
        # Pause briefly to let player see result
        time.sleep(2.0)
    
    def _ai_turn(self):
        """Handle the AI's turn including attack and result display."""
        # Display boards before AI turn
        self.ui.clear_screen()
        cpu_ship_parts = {name: ship.positions for name, ship in self.ai.board.ships.items()}
        self.ui.display_boards(self.player.board, self.ai.board, cpu_ship_parts)
        
        # AI's turn announcement
        cprint("AI Turn", "magenta", attrs=["bold"])
        time.sleep(0.5)
        
        # Execute AI attack
        result, _ = self.ai.attack(self.player.board, self.sound_manager)
        
        # Display attack result
        if result:
            cprint(result, "green" if "Hit" in str(result) or "destroyed" in str(result) else "red")
        else:
            cprint("AI made an invalid move!", "red")
        
        # Show boards after AI turn
        time.sleep(2.0)
        
        self.ui.display_boards(self.player.board, self.ai.board, cpu_ship_parts)
        time.sleep(0.5)
        self.ui.clear_screen()
    
    def _handle_player_win(self):
        """
        Handle the game ending with player victory.
        Creates an immersive, emotional victory sequence with retro military aesthetics.
        """
        self.ui.clear_screen()
    
        # Play victory sound
        self.sound_manager.play_win()
    
        # Animated mission accomplished banner
        victory_banner = """
        ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗
        ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║
        ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║
        ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝
         ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗
          ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝
        """
    
        # Ship ASCII art for victory
        victory_ship = """
                            |    |    |                 
                           )_)  )_)  )_)              
                          )___))___))___)\            
                         )____)____)_____)\\
                   _____|____|____|____|____\\\__
          ---------\                   /--------- \\
            ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
              ^^^^      ^^^^     ^^^    ^^
                   ^^^^      ^^^
        """
    
        # Dramatic mission success readout
        for i in range(3):
            self.ui.clear_screen()
            time.sleep(0.2)
            cprint("\n\n  MISSION STATUS: ", "white", end="")
            cprint("CALCULATING...", "yellow", attrs=["blink"])
            time.sleep(0.3)
    
        # Victory animation
        self.ui.clear_screen()
    
        # Flash "MISSION ACCOMPLISHED" in different colors
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        for color in colors:
            self.ui.clear_screen()
            cprint("\n\n  MISSION STATUS: ", "white", end="")
            cprint("ACCOMPLISHED", color, attrs=["bold"])
            time.sleep(0.2)
    
        # Display victory banner with triumphant music
        self.ui.clear_screen()
        cprint(victory_banner, "green", attrs=["bold"])
        cprint("\n                 ★ MISSION ACCOMPLISHED ★", "yellow", attrs=["bold"])
        cprint(victory_ship, "cyan")
    
        # Detailed victory report
        cprint("\n╔════════════════════════════════════════════════════════════════════════╗", "blue")
        cprint("║                     NAVAL INTELLIGENCE REPORT                          ║", "blue")
        cprint("╠════════════════════════════════════════════════════════════════════════╣", "blue")
    
        # Dramatic typing effect for the victory message
        victory_messages = [
            "║ TRANSMISSION FROM HIGH COMMAND:                                        ║",
            "║                                                                        ║",
            "║ Admiral, your tactical brilliance has secured a decisive victory.      ║",
            "║ The enemy fleet has been completely neutralized.                       ║",
            "║                                                                        ║",
            "║ Our intelligence analysts report all enemy vessels have been           ║",
            "║ confirmed destroyed. Your name will be recorded in the annals of       ║",
            "║ naval warfare as one of history's greatest commanders.                 ║",
            "║                                                                        ║",
            "║ The President extends personal congratulations for your service.       ║",
            "║                                                                        ║",
            "║ MISSION OUTCOME: TOTAL VICTORY                                         ║"
        ]
    
        for line in victory_messages:
            time.sleep(0.3)
            cprint(line, "white")
    
        cprint("╚════════════════════════════════════════════════════════════════════════╝", "blue")
    
        # Medal of honor notification with flashing effect
        for i in range(4):
            if i % 2 == 0:
                cprint("\n              ★★★ MEDAL OF HONOR AWARDED ★★★", "yellow", attrs=["bold"])
            else:
                cprint("\n              ☆☆☆ MEDAL OF HONOR AWARDED ☆☆☆", "white", attrs=["bold"])
            time.sleep(0.4)
    
        # Final congratulations
        cprint("\nYou have demonstrated exceptional strategic thinking and bravery.", "green")
        cprint("Your country thanks you for your service.", "green")
    
        # Pause to let the player savor the victory
        time.sleep(1)
        cprint("\n[PRESS ENTER TO CONTINUE]", "white", attrs=["blink"])
        input()
    
        self.ui.clear_screen()
    
    def _handle_ai_win(self):
        """
        Handle the game ending with AI victory.
        Creates a somber, dramatic defeat sequence with retro military aesthetics.
        """
        self.ui.clear_screen()
    
        # Play defeat sound
        self.sound_manager.play_gameover()
    
        # Animated mission failed banner
        defeat_banner = """
        ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗    
        ████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║    
        ██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║    
        ██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║    
        ██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║    
        ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    
        ███████╗ █████╗ ██╗██╗     ███████╗██████╗             
        ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗            
        █████╗  ███████║██║██║     █████╗  ██║  ██║            
        ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║            
        ██║     ██║  ██║██║███████╗███████╗██████╔╝            
        ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝             
        """
    
        # Sinking ship ASCII art for defeat
        defeat_ship = """
                                ____
                       _____   /   /\\
                      / ____\\ /___/  \\      
           ~~~~~~~~~~~\\      \\     D~~~~~~~~~~~~~~
        ~~~~    ~~~    \\______\\_____\\  ~~~    ~~~
            ~~~~    ~~~    ~~~    ~~~~    ~~~
                ~~~~    ~~~    ~~~    ~~~~
                    ~~~~    ~~~    ~~~
        """
    
        # Dramatic mission failure sequence
        for i in range(3):
            self.ui.clear_screen()
            time.sleep(0.2)
            cprint("\n\n  FLEET STATUS: ", "white", end="")
            cprint("CRITICAL", "red", attrs=["blink"])
            time.sleep(0.4)
    
        # Alarm sequence
        self.ui.clear_screen()
        for i in range(4):
            if i % 2 == 0:
                cprint("\n\n\n            !!! ALERT - VESSELS UNDER HEAVY FIRE !!!", "red", attrs=["bold"])
            else:
                cprint("\n\n\n            --- ALERT - VESSELS UNDER HEAVY FIRE ---", "white", attrs=["bold"])
            time.sleep(0.3)
    
        # Loss confirmation with dramatic effect
        self.ui.clear_screen()
        time.sleep(0.5)
    
        cprint("\n\n  FLEET STATUS: ", "white", end="")
        time.sleep(0.7)
        cprint("LOST", "red", attrs=["bold"])
        time.sleep(1.5)
    
        # Display defeat banner with somber music continuing
        self.ui.clear_screen()
        cprint(defeat_banner, "red")
        cprint("\n                 ■ MISSION FAILED ■", "white")
        cprint(defeat_ship, "blue")
    
        # Detailed defeat report
        cprint("\n╔════════════════════════════════════════════════════════════════════════╗", "red")
        cprint("║                EMERGENCY TRANSMISSION - PRIORITY ALPHA                 ║", "red")
        cprint("╠════════════════════════════════════════════════════════════════════════╣", "red")
    
        # Dramatic typing effect for the defeat message
        defeat_messages = [
            "║ TO: NAVAL HIGH COMMAND                                                 ║",
            "║ FROM: RESCUE VESSEL 'VIGILANT'                                         ║",
            "║                                                                        ║",
            "║ We regret to inform command that the fleet has been lost.              ║",
            "║ Enemy forces demonstrated superior tactical positioning.               ║",
            "║                                                                        ║",
            "║ All vessels confirmed sunk. Search and rescue operations               ║",
            "║ are underway for survivors.                                            ║",
            "║                                                                        ║",
            "║ Request immediate reinforcements to secure the sector.                 ║",
            "║                                                                        ║",
            "║ MISSION OUTCOME: DEFEAT                                                ║"
        ]
    
        for line in defeat_messages:
            time.sleep(0.3)
            cprint(line, "white")
    
        cprint("╚════════════════════════════════════════════════════════════════════════╝", "red")
    
        # Slow static effect to simulate damaged communications
        for i in range(3):
            cprint("\n*kzzzt* ... *static* ... *communication unstable*", "white")
            time.sleep(0.5)
    
        # Encouragement for next attempt
        cprint("\n╔════════════════════════════════════════════════════════════════════════╗", "yellow")
        cprint("║                         ENCRYPTED MESSAGE                              ║", "yellow")
        cprint("╠════════════════════════════════════════════════════════════════════════╣", "yellow")
        cprint("║                                                                        ║", "white")
        cprint("║  Admiral, though we've suffered a defeat today, the war continues.     ║", "white")
        cprint("║                                                                        ║", "white")
        cprint("║  Study the enemy's tactics. Regroup. Plan a new strategy.              ║", "white")
        cprint("║                                                                        ║", "white")
        cprint("║  High Command awaits your return to battle.                            ║", "white")
        cprint("║                                                                        ║", "white")
        cprint("╚════════════════════════════════════════════════════════════════════════╝", "yellow")
    
        # Pause to let the player absorb the defeat
        time.sleep(1)
        cprint("\n[PRESS ENTER TO CONTINUE]", "white", attrs=["blink"])
        input()
    
        self.ui.clear_screen()
    
    def reset_game(self):
        """Reset the game for another round."""
        # Create new boards
        self.player = Player("Player")
    
        # Keep the same difficulty but reset the AI
        difficulty = self.ai.difficulty
        self.ai = AIPlayer(difficulty)
    
        # Ask how player wants to place ships
        placement_method = self.ui.get_placement_choice()
    
        # Set up boards
        self.ai.setup()  # AI always uses random placement
        self.player.setup(placement_method, self.ui, self.sound_manager)

    def post_game_menu(self):
        """Display the post-game menu with options to restart or quit."""
        while True:
            self.ui.clear_screen()
        
            cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "cyan")
            cprint("║                                 MISSION DEBRIEF                               ║", "cyan", attrs=["bold"])
            cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "cyan")
            cprint("║  Your current deployment has concluded. Select your next action:              ║", "white")
            cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "cyan")
        
            # Option 1: Return to main menu
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "green")
            cprint("│ 1. RETURN TO COMMAND CENTER                                                  │", "green", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "green")
            cprint("│  Return to main briefing room to select new mission parameters               │", "white")
            cprint("│  • Choose new difficulty setting                                             │", "white")
            cprint("│  • Select new fleet deployment strategy                                      │", "white")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "green")
        
            # Option 2: Quit game
            cprint("\n┌─────────────────────────────────────────────────────────────────────────────┐", "red")
            cprint("│ 2. END NAVAL OPERATIONS                                                      │", "red", attrs=["bold"])
            cprint("├─────────────────────────────────────────────────────────────────────────────┤", "red")
            cprint("│  Conclude all naval operations and return to base                            │", "white")
            cprint("└─────────────────────────────────────────────────────────────────────────────┘", "red")
        
            # Get player choice
            cprint("\n[AWAITING COMMAND] Enter your selection (1 or 2): ", "cyan", attrs=["bold"])
            choice = input().strip()
        
            if choice == "1":
                return "main_menu"
            elif choice == "2":
                return "quit"
            else:
                cprint("\nInvalid selection. Please enter 1 or 2.", "red")
                time.sleep(1.5)
    def show_exit_screen(self):
        """
        Display a visually impressive exit screen when player quits the game.
        Uses naval themes and military styling for an appropriate sendoff.
        """
        self.ui.clear_screen()
        sailing_away = """
                                         |__
                                         |\/
                                         ---
                                         / | [
                                  !      | |||
                                _/|     _/|-++'
                            +  +--|    |--|--|_ |-
                         { /|__|  |/\__|  |--- |||__/
                        +---------------___[}-_===_.'____                 /\\
                    ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
     __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
    |                                                                          /
     \_________________________________________________________________________|
                                          SAILING HOME
        """
    
        # Display the banner and ship with appropriate colors
        self.ui.clear_screen()
        cprint(sailing_away, "cyan")
    
    
        # Game credits with military formatting
        time.sleep(0.5)
        cprint("\n╔══════════════════════════════════════════════════════════════════════════════╗", "cyan")
        cprint("║                              MISSION CREDITS                                 ║", "cyan", attrs=["bold"])
        cprint("╠══════════════════════════════════════════════════════════════════════════════╣", "cyan")
        cprint("║  BATTLESHIP TACTICAL COMMAND SYSTEM v1.0                                     ║", "white")
        cprint("║  DEVELOPED BY ZYLO_X STUDIOS                                                 ║", "white")
        cprint("║                                                                              ║", "white")
        cprint("║  COMBAT ENGAGEMENTS: CLASSIFIED                                              ║", "white")
        cprint("║  MISSION STATUS: COMPLETE                                                    ║", "white")
        cprint("╚══════════════════════════════════════════════════════════════════════════════╝", "cyan")
    
        # System shutdown sequence
        time.sleep(1)
        cprint("\n[SYSTEM SHUTDOWN SEQUENCE]", "red")
    
        shutdown_sequence = [
            "Disconnecting from tactical network...",
            "Encrypting mission logs...",
            "Securing classified data...",
            "Deactivating command interface...",
            "Powering down naval computer systems..."
        ]
    
        for line in shutdown_sequence:
            time.sleep(0.2)
            cprint("  " + line, "white")
            # Display dots for processing effect
            for _ in range(3):
                cprint(".", "white", end="", flush=True)
                time.sleep(0.1)
            cprint(" [COMPLETE]", "green")
    
        # Final goodbye
        time.sleep(0.2)
        cprint("\n[FINAL MESSAGE]", "cyan", attrs=["bold"])
    
        final_message = "THANK YOU FOR YOUR SERVICE, COMMANDER. SYSTEM SHUTTING DOWN."
    
        # Type out the final message character by character
        for char in final_message:
            cprint(char, "cyan", end="", flush=True)
            time.sleep(0.05)
    
        # Wait for a moment before final exit
        time.sleep(1)
        self.ui.clear_screen()
    
        # One last flashing message
        for i in range(4):
            self.ui.clear_screen()
            time.sleep(0.2)
            if i % 2 == 0:
                cprint("\n\n\n            >>> BATTLESHIP COMMAND TERMINATED <<<", "red", attrs=["bold"])
            else:
                cprint("\n\n\n            --- BATTLESHIP COMMAND TERMINATED ---", "white", attrs=["bold"])
            time.sleep(0.2)

    def start(self):
        """
        Main game loop with proper menu flow.
        """
        show_intro = True
        running = True
    
        while running:
            if show_intro:
                # Only show intro the first time
                self.ui.attempt_fullscreen()    
                self.ui.loading_screen()
                self.ui.ship_screen()
                self.sound_manager.play_intro()
                self.ui.display_rules()
                show_intro = False  # Don't show intro again
        
            # Get difficulty
            difficulty = self.ui.select_difficulty()
            self.ai = AIPlayer(difficulty)
        
            # Create the player
            self.player = Player("Player")
        
            # Get placement method
            placement_method = self.ui.get_placement_choice()
        
            # Set up boards
            self.ai.setup()  # AI always uses random placement
            self.player.setup(placement_method, self.ui, self.sound_manager)
        
            # Stop intro sound if still playing
            self.sound_manager.stop_intro()
            self.ui.clear_screen()
        
            # Play the game
            self.play_game()
        
            # Show post-game menu
            choice = self.post_game_menu()
        
            if choice == "quit":
                self.show_exit_screen()  # Show the goodbye screen
                running = False  # Exit the game
            # If choice is "main_menu", the loop continues
    # Run the game when script is executed
if __name__ == "__main__":
    
    game = BattleshipGame()
    game.start()
