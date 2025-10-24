🖼️ PiP Player: Always-On-Top Web Browser v1.0.0

A lightweight, persistent Picture-in-Picture (PiP) utility built with Python and PyQt6. This app is designed to float above all other applications, making it perfect for watching videos, streaming, or monitoring web content while you work.

✨ Key Features

True PiP (Always On Top): The window maintains a high Z-order, staying visible above all other applications (full-screen apps, IDEs, documents).

Persistent Session: Securely saves login credentials, cookies, and history to a dedicated local folder (~/.PiP_Session_Data), ensuring you stay signed in between sessions.

Native Window Controls: Includes standard Minimize and Close buttons for smooth integration with macOS and Windows.

Minimal Interface: The URL input bar automatically hides after navigation. Right-click anywhere on the video content to reveal the URL bar again.

Fast Startup: Uses the optimized PyInstaller --onedir mode for quick launch times.

💻 Installation & Usage

Option A: Ready-to-Use Download

Platform

Status

Download

macOS

Release Available

Download the PiP_Player_macOS.zip file from the Assets section below. Unzip it and place the PiP Player.app in your Applications folder.

Windows

Coming Soon

The Windows executable is currently being compiled and tested. Please use Option B for now, or check back soon for the release!

To launch, simply double-click the application.

Option B: From Source (Linux/Advanced Users)

Dependencies: Ensure Python 3 is installed, then install the required libraries:

pip install PyQt6 PyQt6-WebEngine


Run: Execute the source file:

python pip_window.py


🛠️ Known Limitation on macOS (Mission Control)

Due to the way macOS handles "Always On Top" windows, the PiP Player window will not drag across desktop spaces using the Mission Control mouse gesture.

Workaround: To move the window to an adjacent desktop space, enter Mission Control, select the PiP window, and use the keyboard shortcut: Control + Left Arrow or Control + Right Arrow.

📦 Bundling Command (For Maintainers)

The application is bundled using PyInstaller with the following command to ensure stability and speed:

pyinstaller --onedir --windowed --name "PiP Player" --hidden-import PyQt6.QtWebEngineWidgets pip_window.py
