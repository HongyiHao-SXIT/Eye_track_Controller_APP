import sys
from PyQt6.QtWidgets import QApplication
from main_window import CodeSnakeMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CodeSnakeMainWindow()
    window.show()
    sys.exit(app.exec())