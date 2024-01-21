from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar, QToolBar, QGridLayout, QPushButton, QWidget

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
        helloMsg = QLabel("<h1>Hello, World!</h1>")
        layout.addWidget(helloMsg, 0, 0, 1, 3)
        layout.addWidget(QPushButton("Left"), 2, 0)
        layout.addWidget(QPushButton("Center"), 2, 1)
        layout.addWidget(QPushButton("Right"), 2, 2)
        window.setLayout(layout)
        self.setCentralWidget(window)

        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
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