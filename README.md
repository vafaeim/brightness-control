<h1 align="center">Brightness Control</h1>
<h3 align="center">Designed for <code>Linux-based systems</code>.</h3>
<p align="center">
  <img src="img/app_screenshot.png" alt="App Screenshot">
</p>

<p align="center">
  <strong>Simplify Screen Brightness Adjustment with the Brightness Control</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#usage">Usage</a> •
  <a href="#themes">Themes</a> •
  <a href="#troubleshooting">Troubleshooting</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>


## Features

- **Intuitive Brightness Control:** Elevate your screen experience with a beautifully designed interface, enabling effortless adjustment of brightness levels.

- **Real-Time Feedback:** As you interact with the slider, the application instantly displays the ongoing brightness percentage, aiding precision.

- **Seamless Brightness Application:** One click on the "Apply Brightness" button seamlessly enacts the selected brightness setting, leveraging the powerful `brightnessctl` utility.

- **Personalized Themes:** Embrace your visual preferences by selecting between 10 elegant themes.

- **Immediate Utility Status:** Stay informed about the `brightnessctl` utility's availability through real-time feedback, ensuring you're always ready to manage brightness.

- **Community Collaboration:** As an open-source project, the app encourages community participation, from suggesting improvements to contributing code.

---

## Getting Started

### Prerequisites

Before using the Brightness Control, make sure you have the following prerequisites installed:
- **Linux-based system:** Brightness Control designed for Linux-based systems.

- **Python 3.x:** If not installed, download the latest version from [python.org](https://www.python.org/downloads/).

- **PyQt5:** Install the PyQt5 package using the following command:
  ```sh
  pip install pyqt5
  ```

- **brightnessctl Utility:** This app relies on the `brightnessctl` utility. Install it based on your Linux distribution:

  - **For Ubuntu/Debian-based Systems:**
    ```sh
    sudo apt-get install brightnessctl
    ```

  - **For Arch-based Systems:**
    ```sh
    sudo pacman -S brightnessctl
    ```

  - **For Fedora-based Systems:**
    ```sh
    sudo dnf install brightnessctl
    ```

  - **For openSUSE-based Systems:**
    ```sh
    sudo zypper install brightnessctl
    ```

  - **For CentOS/RHEL-based Systems:**
    ```sh
    sudo yum install brightnessctl
    ```



### Installation

**Note: Brightness Control is designed for Linux-based systems.**

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/vafaeim/brightness-control.git
   ```

2. **Navigate to the Project Directory:**
   ```sh
   cd brightness-control
   ```

3. **Run the Application:**
   ```sh
   python src/main.py
   ```

---

## Usage

1. **Launch the Application:**
   The app welcomes you with a beautifully crafted interface, inviting you to take control of your screen's brightness.

2. **Adjust Brightness:**
   - Use the slider to make nuanced brightness adjustments.
   - Witness the real-time brightness preview for accurate fine-tuning.

3. **Apply Brightness:**
   - When satisfied with the desired brightness, clicking the "Apply Brightness" button affects the change.

---

## Themes

  1. Locate the "Theme" option on the menu bar.
  2. Click on it to reveal a dropdown menu.
  3. Within the dropdown, you can choose from available themes.
  ##### Currently, there are options for dark mode, silver, blue, purple green, red, yellow, orange, brown, pink, 

---

## Troubleshooting

Encountering issues? Follow these steps to troubleshoot:

- **Check brightnessctl Installation:** Ensure `brightnessctl` is correctly installed and accessible in your terminal.

- **Permissions:** Verify you possess the necessary permissions to adjust brightness. In some scenarios, superuser privileges may be required.

- **Theme Concerns:** If theme-related problems emerge, confirm that the theme stylesheet files (`dark_theme.qss`, `blue_theme.qss`, etc.) reside alongside `main.py`.

---

## Contributing

Welcome contributions! To enhance the app:

- Submit a pull request for functional improvements or new features.

- Open an issue for bug reports or discussions about enhancements.

---

## License

This project is licensed under the MIT License. For details, please look at the [LICENSE](LICENSE) file.

---

<p align="center">
  Created with ❤️ by Amirreza Vafaei Moghadam
</p>
<p align="center">
  For questions or feedback, you can reach out at
  <a href="mailto:vafaeim@icloud.com">vafaeim@icloud.com</a>.
</p>

# brightness-control
