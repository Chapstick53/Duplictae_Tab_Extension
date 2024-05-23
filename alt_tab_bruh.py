import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
import win32gui
import win32con
import time


class AlwaysOnTopButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowOpacity(0.5)  # Set window opacity (transparency)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # Set window always on top

        self.button = QPushButton('Switch Windows', self)
        self.button.clicked.connect(self.switch_windows)

        self.setGeometry(300, 300, 200, 100)  # Set window geometry
        self.setWindowTitle('Always On Top Button')
        self.show()

    def switch_windows(self):
        # Find window handles for Window A and Window B
        hwnd_a = win32gui.FindWindow(None, "Window A Title")
        hwnd_b = win32gui.FindWindow(None, "Window B Title")

        # Get current foreground window handle
        current_hwnd = win32gui.GetForegroundWindow()

        # Switch from A to B or from B to A
        if current_hwnd == hwnd_a:
            win32gui.SetForegroundWindow(hwnd_b)
        elif current_hwnd == hwnd_b:
            win32gui.SetForegroundWindow(hwnd_a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlwaysOnTopButton()
    sys.exit(app.exec_())
