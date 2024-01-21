from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar, QToolBar, QGridLayout, QPushButton, QWidget
from functools import partial

class Window(QMainWindow):
    """PyCalc window or elements layout class.

    PyCalc window or elements layout class which contains the main application
    layout logic.

    Attributes:
        none

    Methods:
        __init__         - class method to create a new window
        _createMenu      -
        _createToolBar   -
        _createStatusBar -

    """
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
        window = QWidget()
        layout = QGridLayout()
        self.helloMsg = QLabel("<h1>Hello, World!</h1>")
        layout.addWidget(self.helloMsg, 0, 0, 1, 3)
        
        left = QPushButton("Left")
        left.clicked.connect(partial(self.button_clicked, "Left"))
        layout.addWidget(left, 2, 0)

        center = QPushButton("Center")
        center.clicked.connect(partial(self.button_clicked, "Center"))
        layout.addWidget(center, 2, 1)

        right = QPushButton("Right")
        right.clicked.connect(partial(self.button_clicked, "Right"))
        layout.addWidget(right, 2, 2)

        window.setLayout(layout)
        self.setCentralWidget(window)

        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        pass

    def button_clicked(self, inputData: str):
        """this function is an event responder for buttons in the app
    
        This function is an event responder for buttons in the app. It is called
        when a button is clicked with data from the clicked button.

        Parameters
        ----------
        inputData - data from the clicked object

        Returns
        -------
        none
        """
        self.helloMsg.setText(f"<h1>Hello World. {inputData} button clicked!</h1>")  
        pass    
        
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)