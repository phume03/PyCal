# 1. Import QApplication, and all the required widgets
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QHBoxLayout, QPushButton, QWidget, QVBoxLayout

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

vlayout = QVBoxLayout()
helloMsg = QLabel("<h1>Hello, World!</h1>")
vlayout.addWidget(helloMsg)

# QVBoxLayout refuses to take another layout widget as a parameter, so the code below breaks
#hlayout = QHBoxLayout()
#hlayout.addWidget(QPushButton("Left"))
#hlayout.addWidget(QPushButton("Center"))
#hlayout.addWidget(QPushButton("Right"))

#vlayout.addWidget(hlayout)
window.setLayout(vlayout)



# 4.Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())