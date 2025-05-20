# 🚢 BATTLESHIPS

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.7%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-green)


                            █████████████████████████████████████████████████████████
                            █▄─▄─▀██▀▄─██─▄─▄─█─▄─▄─█▄─▄███▄─▄▄─█─▄▄▄▄█─█─█▄─▄█▄─▄▄─█
                            ██─▄─▀██─▀─████─█████─████─██▀██─▄█▀█▄▄▄▄─█─▄─██─███─▄▄▄█
                            ▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄a▄▄▄▀▄▀▄▀▄▄▄▀▄▄▄▀▀▀
                          

A modern, feature-rich implementation of the classic Battleships game designed for terminal/console play. Featuring an advanced AI opponent, immersive sound effects, and a retro command-console aesthetic.

```
                                                         # #  ( )
                                                      ___#_#___|__
                                                  _  |____________|  _
                                           _=====| | |            | | |==== _
                                     =====| |.---------------------------. | |====
                       <--------------------'   .  .  .  .  .  .  .  .   '--------------/
                         \                                                             /
                          \___________________________________________________________/
```

## ✨ Features

- **Object-Oriented Design**: Clean, modular code architecture
- **Advanced AI**: Two difficulty levels with smart targeting algorithms
- **Colorful Terminal UI**: Beautiful ASCII art with colored output
- **Sound Effects**: Immersive audio for hits, misses, and game events
- **Detailed Battle Statistics**: Track your accuracy and enemy ship status
- **Dramatic Victory/Defeat Sequences**: Cinematic endings with animation effects
- **Custom Ship Visuals**: Unique emoji identifiers for each vessel type

## 🔧 Requirements

- Python 3.7 or higher
- Required packages:
  - pygame
  - termcolor
  - pyfiglet

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/zylo-X/Battleships-Tactical.git
cd Battleships-Tactical
```

2. Install required packages:
```bash
pip install pygame termcolor pyfiglet
```

3. Run the game:
```bash
python Battleships.py
```

## 🎮 How to Play

1. **Launch the Game**: Run `Battleships.py`
2. **Read the Rules**: The game will display detailed instructions
3. **Choose Difficulty**: Select between Normal and Hard mode
4. **Ship Placement**: Your ships will be automatically placed
5. **Target Enemy Ships**: Input row and column coordinates to attack
6. **Sink All Ships**: Destroy all enemy vessels before they destroy yours!

## 🎯 Game Rules

- **Battlefield**: Two 10x10 grids representing your fleet and enemy fleet
- **Ships**: 5 ships of different sizes (Carrier, Battleship, Cruiser, Submarine, Destroyer)
- **Gameplay**: Players take turns firing at coordinates on the opponent's grid
- **Hit Indicators**: 💥 = Hit, ⭕ = Miss, 🟦 = Unexplored
- **Winning**: Sink all enemy ships before they sink yours!

## 🧠 AI Difficulty Levels

- **Normal**: Random targeting
- **Hard**: Intelligent targeting with probability mapping and ship direction analysis

## 🏗️ Technical Implementation

The game is built using the following architecture:

- **UI Class**: Handles all display and input operations
- **SoundManager**: Controls game audio and effects
- **Ship**: Represents individual vessels with positions and damage tracking
- **Board**: Manages the game grid, ship placement, and attack registration
- **Player/AIPlayer**: Handles player actions and AI strategy
- **BattleshipGame**: Coordinates overall game flow

The Hard AI uses several algorithms:
- Probability density mapping
- Target prioritization
- Ship orientation detection
- Optimal target selection

## 🛠️ Project Structure

```
Battleships/
│
├── Battleships.py       # Main game file
├── Assets/              # Game audio files
│   ├── intro.mp3        # Intro music
│   ├── Hit.mp3          # Hit sound effect
│   ├── miss.mp3         # Miss sound effect
│   ├── win.mp3          # Victory music
│   └── gameover.mp3     # Defeat music
│
└── README.md            # Documentation
```

## 🎵 Audio Credits
opengameart
Sound effects and music are included for an immersive gaming experience.

## 🔍 Code Highlights

- **Object-Oriented Implementation**: Clean separation of concerns
- **Advanced AI Logic**: Sophisticated targeting algorithms for the hard difficulty
- **Immersive UI Design**: Retro command-console aesthetic
- **Detailed Documentation**: Comprehensive comments and docstrings

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎨 Credits

Developed by ZYLO-X STUDIOS © 2025

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/zylo-X">ZYLO-X</a>
</p>
