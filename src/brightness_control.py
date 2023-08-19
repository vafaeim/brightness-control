import sys
import subprocess
from PyQt5.QtWidgets import QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget, QPushButton, QMessageBox, QMenuBar, QMenu, QHBoxLayout, QApplication, QDialog
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QIcon, QFont
from about_dialog import AboutDialog

# Define the main application window
class BrightnessControl(QMainWindow):
    MIN_BRIGHTNESS = 20
    MAX_BRIGHTNESS = 976
    
    def __init__(self):
        super().__init__()
        
        # Initialize application settings
        self.settings = QSettings("ifago", "BrightnessControl")
        
        # Set up the main user interface
        self.init_ui()
        
    def init_ui(self):
        # Set up the main window properties
        self.setWindowTitle("Brightness Control")
        self.setGeometry(100, 100, 375, 275)
        self.setFixedSize(self.size())
        
        # Set the window icon
        icon = QIcon('img/logo.ico')
        self.setWindowIcon(icon)
        
        # Initialize UI components
        self.create_widgets()
        self.create_layouts()
        self.create_menu()
        self.check_brightnessctl()

    # Create UI widgets
    def create_widgets(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Title label for the brightness adjustment section
        self.title_label = QLabel("Adjust Brightness", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        
        # Status label to provide feedback on the brightness control utility
        self.status_label = QLabel("Checking...", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Label to display the current brightness level
        self.brightness_label = QLabel("50%", self)
        self.brightness_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Slider for adjusting the brightness
        self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(50)
        self.brightness_slider.valueChanged.connect(self.update_brightness_label)
        
        # Button to apply the selected brightness level
        self.apply_button = QPushButton("Apply Brightness", self)
        self.apply_button.setObjectName("applyButton")
        self.apply_button.setToolTip("Apply the selected brightness level")
        self.apply_button.clicked.connect(self.apply_brightness)

    # Set up the layout of UI components
    def create_layouts(self):
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.title_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.brightness_label)
        layout.addWidget(self.brightness_slider)
        layout.addWidget(self.apply_button)
        self.central_widget.setLayout(layout)

    # Create the application menu
    def create_menu(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        # File menu for quitting the application
        self.file_menu = self.menu_bar.addMenu("File")
        self.file_menu.addAction("Quit", self.close)
        
        # Theme menu for selecting different UI themes
        self.view_menu = self.menu_bar.addMenu("Theme")
        self.dark_theme_action = self.view_menu.addAction("Dark Theme")
        self.green_theme_action = self.view_menu.addAction("Green Theme")
        self.blue_theme_action = self.view_menu.addAction("Blue Theme")
        self.red_theme_action = self.view_menu.addAction("Red Theme")
        
        # Connect actions to theme selection methods
        self.dark_theme_action.triggered.connect(self.load_dark_theme)
        self.green_theme_action.triggered.connect(self.load_green_theme)
        self.blue_theme_action.triggered.connect(self.load_blue_theme)
        self.red_theme_action.triggered.connect(self.load_red_theme)
        
        # About menu for displaying application information
        self.about_menu = self.menu_bar.addMenu("About")
        self.about_menu.addAction("About", self.show_about_dialog)


    # Load the dark theme stylesheet
    def load_dark_theme(self):
        with open("themes/dark_theme.qss", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            self.app.setStyleSheet(stylesheet)
    
    # Load the green theme stylesheet
    def load_green_theme(self):
        with open("themes/green_theme.qss", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            self.app.setStyleSheet(stylesheet)

    # Load the blue theme stylesheet
    def load_blue_theme(self):
        with open("themes/blue_theme.qss", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            self.app.setStyleSheet(stylesheet)

    # Load the red theme stylesheet
    def load_red_theme(self):
        with open("themes/red_theme.qss", "r") as stylesheet_file:
            stylesheet = stylesheet_file.read()
            self.app.setStyleSheet(stylesheet)
    
    # Show the about dialog
    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    # Check if the brightness control utility (brightnessctl) is installed
    def check_brightnessctl(self):
        try:
            # Check if 'brightnessctl' is available using its help command
            subprocess.run("brightnessctl --help", shell=True, check=True)
            # Indicate successful installation with a green status label
            self.status_label.setStyleSheet("color: #27ae60;")
            self.status_label.setText("brightnessctl is installed.")
        except subprocess.CalledProcessError as e:
            if e.returncode == 127:
                # Indicate lack of installation with a red status label
                self.status_label.setStyleSheet("color: #f7502f;")
                self.status_label.setText("brightnessctl is not installed.")
    
    # Update the brightness label text when the slider is changed
    def update_brightness_label(self, value):
        brightness_percent = self.brightness_slider.value()
        self.brightness_label.setText(f"{brightness_percent}%")

    # Apply the selected brightness level using 'brightnessctl'
    def apply_brightness(self):
        brightness_value = self.map_slider_to_brightness(self.brightness_slider.value())
        cmd = f"brightnessctl set {brightness_value}"
        try:
            # Run the 'brightnessctl' command to change brightness
            subprocess.run(cmd, shell=True, check=True)
            self.show_success_message()
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            self.show_error_message()

    # Map the slider value to an appropriate brightness value
    def map_slider_to_brightness(self, slider_value):
        brightness_range = self.MAX_BRIGHTNESS - self.MIN_BRIGHTNESS
        return int(self.MIN_BRIGHTNESS + (brightness_range * slider_value / 100))

    # Show a success message after applying brightness
    def show_success_message(self):
        QMessageBox.information(self, "Success", "Brightness applied successfully!")

    # Show an error message if brightness application fails
    def show_error_message(self):
        QMessageBox.critical(self, "Error", "Failed to apply brightness.")

    # Save settings before closing the application
    def closeEvent(self, event):
        self.settings.sync()
        super().closeEvent(event)
