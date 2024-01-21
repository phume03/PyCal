from PyQt6.QtWidgets import QVBoxLayout, QDialog, QDialogButtonBox, QLabel, QGridLayout, QPushButton, QWidget

class Window(QDialog):
    """PyCalc window or elements layout class.

    PyCalc window or elements layout class which contains the main application
    layout logic.

    Attributes:
        none

    Methods:
        __init__ - class method to create a new window

    """

    def __init__(self):
        """this function initiates the calculator window
    
        This function instantiates the window for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        QDialog - A dialog widget

        Returns
        -------
        none
        """
            
        super().__init__(parent=None)
        self.setWindowTitle("PyCalc")
        dialogLayout = QVBoxLayout()
        #window.setGeometry(100, 100, 280, 100)
        layout = QGridLayout()
        helloMsg = QLabel("<h1>Hello, World!</h1>")
        layout.addWidget(helloMsg, 0, 0, 1, 3)
        layout.addWidget(QPushButton("Left"), 2, 0)
        layout.addWidget(QPushButton("Center"), 2, 1)
        layout.addWidget(QPushButton("Right"), 2, 2)
        
        dialogLayout.addLayout(layout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)