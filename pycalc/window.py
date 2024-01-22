from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QMainWindow, QLabel, QStatusBar, QToolBar, QGridLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt
from functools import partial

class Window(QMainWindow):
    """PyCalc window or elements layout class.

    PyCalc window or elements layout class which contains the main application
    layout logic.

    Attributes:
        WINDOW_WIDTH   - width of the calculator window
        WINDOW_HEIGHT  - height of the calculator window
        DISPLAY_HEIGHT - height of the calculator display window
        BUTTON_SIZE    - size of a single calculator button

    Methods:
        __init__         - class method to create a new window
        _createMenu      -
        _createToolBar   -
        _createStatusBar -
        _createDisplay   -
        _createButtons   -

    """
    WINDOW_WIDTH = 230
    WINDOW_HEIGHT = 380
    DISPLAY_HEIGHT = 35
    BUTTON_SIZE = 40

    def __init__(self):
        """this function initiates the calculator window
    
        This function instantiates the window for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        QMainWindow - A main window widget, allows the application to generate a main window–style app
                     as opposed to a dialog style app.

        Returns
        -------
        none
        """   
        super().__init__(parent=None)
        self.setWindowTitle("PyCalc")
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        centralWidget = QWidget(self)
        self.generalLayout = QVBoxLayout()
        
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self._createDisplay()
        self._createButtons()

        pass

    def button_clicked(self, inputData: str):
        """this function is an event responder for buttons in the app
    
        This function is an event responder for buttons in the app. It is called
        when a button is clicked with data from the clicked button.

        Parameters
        ----------
        QMainWindow - A main window widget, allows the application to generate a main window–style app
                     as opposed to a dialog style app.
        inputData - data from the clicked object

        Returns
        -------
        none
        """
        self.helloMsg.setText(f"<h1>Hello World. {inputData} button clicked!</h1>")  
        pass    
        
    def _createMenu(self):
        """this function initiates the calculator window
    
        This function instantiates the window for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        QMainWindow - A main window widget, allows the application to generate a main window–style app
                     as opposed to a dialog style app.

        Returns
        -------
        none
        """   
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        """this function initiates the calculator window
    
        This function instantiates the window for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        QMainWindow - A main window widget, allows the application to generate a main window–style app
                     as opposed to a dialog style app.

        Returns
        -------
        none
        """           
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createStatusBar(self):
        """this function initiates the calculator window
    
        This function instantiates the window for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        QMainWindow - A main window widget, allows the application to generate a main window–style app
                     as opposed to a dialog style app.

        Returns
        -------
        none
        """           
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def _createDisplay(self):
        """creates the display component of the calculator
    
        Creates the display component of the calculator, equivalent of an LCD
        display screen on a physical calculator.

        Parameters
        ----------
        QMainWindow - A main window widget, this is the main panel on which all components will be created initially.

        Returns
        -------
        none
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(self.DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)                  
        pass

    def _createButtons(self):
        """creates the button components of the application
    
        Creates the button components of the calculator.

        Parameters
        ----------
        QMainWindow - A main window widget, which is where all components are initially placed/created.

        Returns
        -------
        none
        """        
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["C", "(", ")", "/"],
            ["pow", "sqrt", "pi", "x"],
            ["7", "8", "9", "-",],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["Del", "0", ".", ""],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                if (key == "="):
                    self.buttonMap[key].setFixedSize(self.BUTTON_SIZE, self.BUTTON_SIZE * 2)
                    buttonsLayout.addWidget(self.buttonMap[key], row, col, 2, 1)
                elif (key == ""):
                    pass
                else:
                    self.buttonMap[key].setFixedSize(self.BUTTON_SIZE, self.BUTTON_SIZE)
                    buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)
        pass

    def setDisplayText(self, UserInput: str):
        """Set the display's text.
    
        Set the text on the display screen for the user.

        Parameters
        ----------
        QMainWindow - A main window widget, which is where all components are initially placed/created.
        UserInput   - Text to display on the calculator display component.

        Returns
        -------
        none
        """ 
        self.display.setText(UserInput)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text.
    
        Retrieve the text presently displayed by the calculator display component.

        Parameters
        ----------
        QMainWindow - A main window widget, which is where all components are initially placed/created.

        Returns
        -------
        Display Text - the text currently displayed by the calculator display screen.
        """ 
        return self.display.text()

    def clearDisplay(self):
        """Clear the display.

        Clear the display component of the calculator.

        Parameters
        ----------
        QMainWindow - A main window widget, which is where all components are initially placed/created.

        Returns
        -------
        none
        """ 
        self.setDisplayText("")    
