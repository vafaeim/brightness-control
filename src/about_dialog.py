from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt5.QtCore import Qt
import sys

# Define a custom dialog for displaying information about the app
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Brightness Control")
        self.setGeometry(200, 200, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # About information text
        about_text = (
            "Brightness Control\n"
            "Version 1.0\n\n"
            "Simplify screen brightness adjustments\n"
            "with Brightness Control. Real-time adjustments,\n"
            "elegant themes, one-click application.\n\n"
            "Contact:\n"
            "vafaeim@icloud.com\n"
            "Amirreza Vafaei Moghadam\n"
            "© 2023 ifago\n"
        )

        # Create a label to display about information
        self.about_label = QLabel(about_text, self)
        self.about_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.about_label)

        # Create an "OK" button to close the dialog
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)


def main():
    app = QApplication(sys.argv)
    about_dialog = AboutDialog()
    about_dialog.exec()

if __name__ == "__main__":
    main()
