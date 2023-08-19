import sys
from PyQt5.QtWidgets import QApplication
from brightness_control import BrightnessControl

# Main function to start the application
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = BrightnessControl()

    # Load the dark theme by default
    window.load_theme("dark")

    # Display the main application window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
