# 1. Import QApplication, and all the required widgets
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout, QPushButton, QWidget

"""PyCalc is a simple calculator built with Python and PyQt.

This is the main file for PyCalc, a simple calculator built with Python and PyQt.


Attributes:
    none

Methods:
    none

"""

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyCalc")
window.setGeometry(100, 100, 280, 100)

layout = QGridLayout()
helloMsg = QLabel("<h1>Hello, World!</h1>")
layout.addWidget(helloMsg, 0, 0, 1, 3)
layout.addWidget(QPushButton("Left"), 2, 0)
layout.addWidget(QPushButton("Center"), 2, 1)
layout.addWidget(QPushButton("Right"), 2, 2)
window.setLayout(layout)

# 4.Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())