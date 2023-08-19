import subprocess
from PyQt5.QtWidgets import QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget, QPushButton, QMessageBox, QAction, QApplication
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QIcon, QFont
from about_dialog import AboutDialog

# Main application window class for controlling brightness
class BrightnessControl(QMainWindow):
    # Minimum and maximum brightness levels for control
    MIN_BRIGHTNESS = 20
    MAX_BRIGHTNESS = 1000

    def __init__(self):
        super().__init__()
        self.app = QApplication.instance()  # Reference to the application instance

        # Initialize application settings
        self.settings = QSettings("ifago", "BrightnessControl")

        # Set up the main user interface
        self.init_ui()

    # Initialize the main user interface
    def init_ui(self):
        self.setWindowTitle("Brightness Control")
        self.setGeometry(100, 100, 375, 275)
        self.setFixedSize(self.size())  # Prevent resizing

        icon = QIcon('img/logo.ico')
        self.setWindowIcon(icon)

        # Initialize UI components
        self.create_widgets()
        self.create_layouts()
        self.create_menu()
        self.check_brightnessctl()

    # Create various UI widgets
    def create_widgets(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.title_label = QLabel("Adjust Brightness", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))

        self.status_label = QLabel("Checking...", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.brightness_label = QLabel("50%", self)
        self.brightness_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(50)
        self.brightness_slider.valueChanged.connect(self.update_brightness_label)

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
        self.menu_bar = self.menuBar()

        self.file_menu = self.menu_bar.addMenu("File")
        self.file_menu.addAction("Quit", self.close)

        self.view_menu = self.menu_bar.addMenu("Theme")

        theme_names = [
            "dark", "silver", "blue", "purple",
            "green", "red", "yellow", "brown",
            "orange", "pink"
        ]

        for theme_name in theme_names:
            action = QAction(f"{theme_name.capitalize()} Theme", self)
            action.triggered.connect(lambda _, theme=theme_name: self.load_theme(theme))
            self.view_menu.addAction(action)

        self.about_menu = self.menu_bar.addMenu("About")
        self.about_menu.addAction("About", self.show_about_dialog)

    # Load a selected UI theme
    def load_theme(self, theme_name):
        stylesheet_path = f"themes/{theme_name}_theme.qss"
        try:
            with open(stylesheet_path, "r") as stylesheet_file:
                stylesheet = stylesheet_file.read()
                self.app.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Theme stylesheet not found: {stylesheet_path}")

    # Show the about dialog
    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    # Check if the brightness control utility (brightnessctl) is installed
    def check_brightnessctl(self):
        try:
            # Check if 'brightnessctl' is available using its help command
            subprocess.run("brightnessctl --help", shell=True, check=True)
            self.status_label.setStyleSheet("color: #27ae60;")  # Indicate successful installation
            self.status_label.setText("brightnessctl is installed.")
        except subprocess.CalledProcessError as e:
            if e.returncode == 127:
                self.status_label.setStyleSheet("color: #f7502f;")  # Indicate lack of installation
                self.status_label.setText("brightnessctl is not installed.")

    # Update the brightness label text when the slider is changed
    def update_brightness_label(self):
        brightness_percent = self.brightness_slider.value()
        self.brightness_label.setText(f"{brightness_percent}%")

    # Apply the selected brightness level using 'brightnessctl'
    def apply_brightness(self):
        brightness_value = self.map_slider_to_brightness(self.brightness_slider.value())
        cmd = f"brightnessctl set {brightness_value}"
        try:
            subprocess.run(cmd, shell=True, check=True)  # Run the 'brightnessctl' command
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
