# Bot Manager

Bot Manager is a simple GUI application for managing and running multiple Python bot scripts. It allows users to add, start, stop, and monitor bot processes easily.

## Features

- Add and manage multiple bot scripts
- Start and stop individual bots
- Auto-start all inactive bots
- Monitor bot status
- Cross-platform support (Windows and Linux)

## Requirements

- Python 3.6+
- tkinter (usually comes pre-installed with Python)
- toml
- psutil

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:

```
pip install toml psutil
```

## Usage

1. Run the main script:

```
python main.py
```

2. The Bot Manager GUI will open.
3. Click "Add Bot" to add a new bot. Enter the bot name and select the Python script file.
4. Use the individual bot buttons to start or stop bots.
5. Use the "AUTO" button to start all inactive bots or stop all active bots.

## Building Executable

### Windows

1. Run the `build.bat` script:

```
build.bat
```

2. Choose the output option (1 for Windows, 2 for Linux).
3. The executable will be created in the `dist` directory.

### Linux

1. Run the `build.sh` script:

```
./build.sh
```

2. Choose the output option (1 for Windows, 2 for Linux).
3. The executable will be created in the `dist` directory.

## Project Structure

```
bot_manager/
│
├── main.py
├── ui/
│   ├── __init__.py
│   ├── app.py
│   └── dialogs.py
├── core/
│   ├── __init__.py
│   ├── bot_manager.py
│   └── config_manager.py
├── utils/
│   ├── __init__.py
│   └── process_manager.py
├── bots.toml
├── build.bat
├── build.sh
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).