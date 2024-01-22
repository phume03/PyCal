from math import sqrt

ERROR_MSG = "ERROR"

def evaluateExpression(expression):
    """Evaluate an expression (Model).
    
    This function evaluates an expression given by the user. This is a model function that
    is called by a controller (circuits) to evaluate an expression taken from the main
    display or the view (window).

    Parameters
    ----------
    expression - a mathematical expression taken from the view to be evaluated

    Returns
    -------
    result - the evaluated mathematical expression
    """ 
    result = ""

    if "sqrt" in expression:
        try:
            result = str(eval(expression))
        except Exception:
            result = ERROR_MSG
    else:
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG

    return result