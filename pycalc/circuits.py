from functools import partial
import math

class PyCalc:
    """PyCalc's controller class.

    PyCalc's controller class. It connects the window (view) to the cpu (model)
    thus completing our Model-View-Controller design pattern arrangement for
    this application.

    Attributes:
        ERROR_MSG - the message to display to screen incase there is a computation error.

    Methods:
        __init__                  - class method to create a new window
        _calculateResult          - a function that computes the desired result from an expression created by the user
        _calculateSquareRootValue - a function that computes the square root value of a value on screen
        _buildExpression          - a function that helps the calculator to build a mathematical expression
        _delFromExpression        - a function that deletes one character from the display
        _connectSignalsAndSlots   - a function that connects buttons to events otherwise known as connecting signals and slots

    """
    ERROR_MSG = "ERROR"

    def __init__(self, model, view):
        """this function initiates the circuits controller
    
        This function instantiates the circuits (controller) for the calculator. It is a class method or a constructor.

        Parameters
        ----------
        model - pycalc's cpu/model
        view  - pycalc's interface/window/view

        Returns
        -------
        none
        """           
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        """this function uses the cpu (model) to compute the desired result from an expression designed by the user
    
        This function uses the cpu (model) to compute the desired result from an expression designed by the user
        and returns the result to the window (view) for display back to the user.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """           
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _calculateSquareRootValue(self):
        """this function uses the cpu (model) to compute the square-root value
    
        This function uses the cpu (model) to compute the square-root value.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        if self._view.displayText() == self.ERROR_MSG:
            self._view.clearDisplay()
        else:
            init_result = self._evaluate(expression=self._view.displayText())
            final_expression = "sqrt("+str(init_result)+")"           
            result = self._evaluate(expression=final_expression)
            self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        """this function helps the calculator to build a mathematical expression
    
        This function helps the calculator to build a mathematical expression from the values pressed
        on the calculator keys, rather than clear the screen and recognise each new press as an
        independent or unique entry to the calculator.

        Parameters
        ----------
        subExpression - the last values entered into the calculator display, without interruption of
                        the clear or clear-screen command.

        Returns
        -------
        none
        """           
        if self._view.displayText() == self.ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _delFromExpression(self):
        """this function removes one character from a mathematical expression
    
        This function helps the calculator to build a mathematical expression by removing
        one character from the characters that were last entered into the screen display.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """           
        if self._view.displayText() == self.ERROR_MSG:
            self._view.clearDisplay()
        else:
            expression = self._view.displayText()[:-1]
            self._view.setDisplayText(expression)        

    def _connectSignalsAndSlots(self):
        """this function connects buttons to events otherwise known as connecting signals and slots
    
        This function connects buttons (slots) to events (signals).

        Parameters
        ----------
        none

        Returns
        -------
        none
        """           
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"C", "pow", "sqrt", "pi", "x", "Del", "="}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
            elif keySymbol == "pow":
                button.clicked.connect(
                    partial(self._buildExpression, "^")
                )
            elif keySymbol == "pi":
                button.clicked.connect(
                    partial(self._buildExpression, str(math.pi))
                )
            elif keySymbol == "x":
                button.clicked.connect(
                    partial(self._buildExpression, "*")
                )
            elif keySymbol == "Del":
                button.clicked.connect(
                    self._delFromExpression
                )
            else:
                pass
                
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
        self._view.buttonMap["sqrt"].clicked.connect(self._calculateSquareRootValue)
        
