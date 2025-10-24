<h1>PiP Player: Always-On-Top Web Browser v1.0.0</h1>

A lightweight, persistent Picture-in-Picture (PiP) utility built with Python and PyQt6. This app is designed to float above all other applications, making it perfect for watching videos, streaming, or monitoring web content while you work.

<h2>✨ Key Features</h2>

- Always On Top: The window maintains a high Z-order, staying visible above all other applications (full-screen apps, IDEs, documents).

- Native Window Controls: Includes standard Minimize and Close buttons for smooth integration with macOS and Windows.

- Persistent Session: Saves login credentials, cookies, and history to a dedicated local folder (~/.PiP_Session_Data), ensuring you stay signed in between sessions.

- Minimal Interface: The URL input bar automatically hides after navigation. Right-click anywhere on the video content to reveal the URL bar.

- Fast Startup: Uses the optimized PyInstaller --onedir mode for quick launch times.

<h2>💻 Installation & Usage</h2>

<h3>Option A: Ready-to-Use Download</h3>

- macOS (Available Now): Download the PiP_Player_macOS.zip file from the Assets section below. Unzip it and place the PiP Player.app in your Applications folder.

- Windows (Coming Soon): The Windows executable is currently being compiled and tested. Please use Option B for now, or check back soon for the release!

Double-click the application to launch.

<h3>Option B: From Source (Recommended for Linux/Advanced Users)</h3>

<h4>Dependencies: Ensure Python 3 is installed, then install the required libraries:</h4>

- pip install PyQt6 PyQt6-WebEngine

Then, Execute the source file: </br>
<code>python pip_window.py</code>



<h2>🛠️ Known Limitation on macOS (Mission Control)</h2>

Due to the way macOS handles "Always On Top" windows, the PiP Player window will not drag across desktop spaces using the Mission Control mouse gesture.

Workaround: To move the window to an adjacent desktop space, enter Mission Control, select the PiP window, and use the keyboard shortcut: Control + Left Arrow or Control + Right Arrow.

<h2>📦 Bundling Command (For Maintainers)</h2>

The application is bundled using PyInstaller with the following command to ensure stability and speed:

<code>pyinstaller --onedir --windowed --name "PiP Player" --hidden-import PyQt6.QtWebEngineWidgets pip_window.py </code>
