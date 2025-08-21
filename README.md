# Project SLVL Game Launcher

![Project SLVL](https://img.icons8.com/dusk/64/steam.png)

A lightweight, powerful launcher for downloading and playing classic Steam games like Counter-Strike 1.6, Half-Life 1, and their legendary mods.

## 🚀 Features

- **One-Click Installation** - Download and install games with a single click
- **Classic Game Preservation** - Access to original versions of legendary titles
- **Mod Support** - Easy installation of popular HL1 mods
- **Portable** - No installation required, just download and run
- **Command Line Access** - Run from anywhere via CMD or PowerShell
- **Beautiful UI** - Colorful terminal interface with ASCII art

## 🎮 Supported Games & Mods

### Main Games
- Counter-Strike 1.6 (Latest Steam version)
- Half-Life 1 (Original and Source versions)
- Condition Zero
- Day of Defeat

### Popular Mods
- Counter-Strike: Zombie Plague
- Gun Game
- Warcraft 3 Mod
- Superhero Mod
- Jailbreak
- Deathrun

## 📦 Installation

### Option 1: Portable Version (Recommended)
1. Download the latest `Project_SLVL.exe` from [Releases](https://github.com/EmadFahim134/Project-SLVL/releases)
2. Run the executable - no installation required!
3. The launcher will automatically create necessary directories

### Option 2: Full Installer
1. Download `Project_SLVL_Setup.exe` from [Releases](https://github.com/EmadFahim134/Project-SLVL/releases)
2. Run the installer and follow the wizard
3. Choose whether to add to system PATH for command line access

## ⌨️ Command Line Usage

After installation, you can run the launcher from anywhere:

```cmd
Project_SLVL
```

## 🖥️ System Requirements

- **OS**: Windows 7/8/10/11 (64-bit recommended)
- **RAM**: 512MB minimum (1GB recommended)
- **Storage**: 2GB free space for games
- **Internet**: Required for downloads

## 🎯 Quick Start

1. **Download** the launcher from Releases
2. **Run** `Project_SLVL.exe`
3. **Browse** the game library using the menu
4. **Select** your desired game or mod
5. **Click Install** and follow the prompts
6. **Launch** your game directly from the launcher

## 📁 Directory Structure

```
C:\Games\
├── Installers\          # Downloaded game installers
├── Half-Life 1.0.0.5\   # Half-Life installation
├── Counter-Strike 1.6\  # CS 1.6 installation  
├── Day of Defeat\       # DoD installation
└── Mods\               # Community mods
```

## 🛠️ Building from Source

### Prerequisites
- Python 3.8+
- Git
- Required packages: `colorama`, `tqdm`, `requests`, `bs4`

### Build Steps

```bash
# Clone the repository
git clone https://github.com/EmadFahim134/Project-SLVL.git
cd Project-SLVL

# Install dependencies
pip install -r requirements.txt

# Build executable
pyinstaller --onefile --console --icon=steam.ico --name "Project_SLVL" --add-data "logo.txt:." main.py
```

## 📝 Usage Guide

### Main Menu Options:
- **1. Install Games** - Download and install supported games
- **2. Launch Games** - Launch already installed games
- **3. Input Urls** - Install games from custom URLs
- **4. Settings** - Configuration options
- **M. Download Modded CS 1.6** - Special modded editions
- **L. View Logs** - See operation history
- **A. About** - Launcher information

### Game Sources:
Games are sourced from trusted providers including:
- https://down-cs.su/
- Official Steam depots (for owned games)
- Community-preserved archives

## 🤝 Contributing

We welcome contributions! Please feel free to submit:
- Bug reports
- Feature requests
- Code improvements
- Game compatibility updates
- Translation support

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ⚠️ Legal Notice

This launcher is designed for:
- Preserving classic game versions
- Educational purposes
- Personal use with owned games

Users are responsible for ensuring they have the rights to download and play any content. The launcher facilitates access to publicly available game files but does not distribute copyrighted content.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/EmadFahim134/Project-SLVL/issues)
- **Discussions**: [GitHub Discussions](https://github.com/EmadFahim134/Project-SLVL/discussions)
- **Email**: [mremad.fahim@gmail.com]

## 📊 Project Status

**Active Development** - Regular updates and new features being added

## 🏆 Credits

**Created by**: EmadFahim134  
**Code Name**: Gordon  
**Version**: 1.0  
**License**: Gnu GPL

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=EmadFahim134/Project-SLVL&type=Date)](https://star-history.com/#EmadFahim134/Project-SLVL&Date)

---

**Experience gaming history with Project SLVL - Where Legends Live On**

*"The right man in the wrong place can make all the difference in the world."* - G-Man

---

*Project SLVL is not affiliated with Valve Corporation or Steam. All game trademarks are property of their respective owners.*
