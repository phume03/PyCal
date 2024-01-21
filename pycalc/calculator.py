# 1. Import QApplication, and all the required widgets
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QHBoxLayout, QPushButton, QWidget

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

#helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
#helloMsg.move(60, 15)

layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)



# 4.Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())