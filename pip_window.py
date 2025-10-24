import sys
import os
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton,
    QMenuBar # Added for potential future use or better macOS integration
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage

# --- Note on Installation ---
# This script requires the PyQt6 library, which must be installed:
# pip install PyQt6 PyQt6-WebEngine
# ---------------------------

class PiPBrowser(QMainWindow):
    """
    A minimal web browser designed for Picture-in-Picture mode that uses native 
    window controls for best macOS integration, multi-desktop drag, and persistence.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PiP Player")
        
        # 1. CRITICAL CHANGE: USE NATIVE WINDOW FLAGS
        # We only keep WindowStaysOnTopHint. Removing FramelessWindowHint restores:
        # - Native Title Bar (with close/min/max buttons)
        # - Ability to drag across Mission Control/Desktops
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        
        # Set an initial, small size typical for PiP
        self.setGeometry(100, 100, 500, 300)

        # --- Persistence Setup ---
        # Define the folder where session data (cookies, cache) will be saved.
        HOME_DIR = os.path.expanduser('~')
        SESSION_DIR = "PiP_Session_Data"
        # Stores data in ~/.PiP_Session_Data
        PROFILE_PATH = os.path.join(HOME_DIR, f".{SESSION_DIR}")
        os.makedirs(PROFILE_PATH, exist_ok=True)
        
        # Create a persistent profile and page
        self.profile = QWebEngineProfile("persistent_pip_profile", self)
        self.profile.setPersistentStoragePath(PROFILE_PATH)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
        
        self.page = QWebEnginePage(self.profile, self)
        # -------------------------

        # Main layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 2. REMOVED: Custom DraggableBar is no longer needed

        # Web Engine View (The actual browser)
        self.browser = QWebEngineView()
        self.browser.setPage(self.page) # Assign the persistent page
        self.browser.setUrl(QUrl("https://www.youtube.com/"))
        self.layout.addWidget(self.browser)
        
        # 3. Control Panel (URL bar only)
        self.control_widget = QWidget()
        self.control_layout = QVBoxLayout(self.control_widget)
        self.control_layout.setContentsMargins(5, 5, 5, 5)
        self.control_widget.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Paste Video URL and Press Enter...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        # REMOVED: Close button, as we now use the native window close button
        
        self.control_layout.addWidget(self.url_bar)

        # Add the control panel to the main layout (below the browser view)
        self.layout.addWidget(self.control_widget)
        
        # Control visibility: only show the control bar initially
        self.control_widget.show()
        self.url_bar.setFocus()
        
        # --- Mouse Event Handling for Controls (Right-Click) ---
        original_browser_press_event = self.browser.mousePressEvent
        
        def new_browser_mouse_press(event):
            # If right click, toggle controls
            if event.button() == Qt.MouseButton.RightButton:
                self.toggle_controls(event)
            # Otherwise, let the web engine handle the event (for clicks on video controls/links)
            else:
                original_browser_press_event(event)

        self.browser.mousePressEvent = new_browser_mouse_press
    
    def closeEvent(self, event):
        """Overrides the default close method to ensure data is saved."""
        self.browser.page().profile().setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
        # Trigger clean exit when the native close button is pressed
        QApplication.quit() 
        super().closeEvent(event)
        
    def navigate_to_url(self):
        """Loads the URL entered in the text box and hides controls."""
        url_text = self.url_bar.text()
        if not url_text.startswith(('http://', 'https://')):
            url_text = 'https://' + url_text
        
        self.browser.setUrl(QUrl(url_text))
        self.control_widget.hide() # Hide controls after navigation
        
    def toggle_controls(self, event):
        """Toggles the visibility of the control panel on right-click."""
        if self.control_widget.isVisible():
            self.control_widget.hide()
        else:
            self.control_widget.show()
            self.url_bar.setFocus()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    try:
        if 'QWebEngineView' not in globals() or not callable(QWebEngineView):
             raise ImportError
    except ImportError:
        print("Error: PyQt6-WebEngine module not found. Please run 'pip install PyQt6 PyQt6-WebEngine'")
        sys.exit(1)
        
    pip_app = PiPBrowser()
    pip_app.show()
    sys.exit(app.exec())
