@echo off
echo Bot Manager Build Script
echo =======================
echo 1. Build for Windows
echo 2. Build for Linux
set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    echo Building for Windows...
    pip install pyinstaller
    pyinstaller --onefile --windowed --add-data "bots.toml;." --name BotManager main.py
    echo Build complete. Executable is in the 'dist' folder.
) else if "%choice%"=="2" (
    echo Building for Linux...
    echo Please run this script on a Linux machine or use WSL.
    echo Here's the command to run on Linux:
    echo ./build.sh
) else (
    echo Invalid choice. Please run the script again and choose 1 or 2.
)

pause