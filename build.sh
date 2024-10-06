#!/bin/bash

echo "Bot Manager Build Script"
echo "======================="
echo "1. Build for Windows"
echo "2. Build for Linux"
read -p "Enter your choice (1 or 2): " choice

if [ "$choice" == "1" ]; then
    echo "Building for Windows..."
    echo "Please run this script on a Windows machine."
    echo "Here's the command to run on Windows:"
    echo "build.bat"
elif [ "$choice" == "2" ]; then
    echo "Building for Linux..."
    pip install pyinstaller
    pyinstaller --onefile --windowed --add-data "bots.toml:." --name BotManager main.py
    echo "Build complete. Executable is in the 'dist' folder."
else
    echo "Invalid choice. Please run the script again and choose 1 or 2."
fi