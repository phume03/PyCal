# 1. Import QApplication, and all the required widgets
import sys
from PyQt6.QtWidgets import QApplication
from pycalc import window

"""PyCalc is a simple calculator built with Python and PyQt.

This is the main file for PyCalc, a simple calculator built with Python and PyQt.


Attributes:
    none

Methods:
    main - launches the calculator by calling on the relevant classes, and initiating the Qt event loop

"""
def main():
    # 2. Create an instance of QApplication
    app = QApplication(sys.argv)

    # 3. Create your application's GUI
    win = window.Window()

    # 4.Show your application's GUI
    win.show()
    
    # 5. Run your application's event loop
    sys.exit(app.exec())

    pass

if __name__ == "__main__":
    print("Testing, running calculator module...")
    main()