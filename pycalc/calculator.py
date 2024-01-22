# 1. Import QApplication, and all the required widgets
import sys
from PyQt6.QtWidgets import QApplication
from pycalc import window, cpu, circuits

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
    displayInterface = window.Window()

    # 4. a.Show your application's GUI
    displayInterface.show()

    # 4. b. connect the display interface, the controller logic, and the cpu/business logic of the application
    circuits.PyCalc(model=cpu.evaluateExpression, view=displayInterface)
    
    # 5. Run your application's event loop
    sys.exit(app.exec())

    pass

if __name__ == "__main__":
    print("Testing, running calculator module...")
    main()