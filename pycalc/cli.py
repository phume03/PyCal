import argparse
from pycalc import __version__, calculator

"""
PyCalc command line interface (cli).

This is an implementation of an interface that will allow users of PyCalc to interact 
with the application in the command line. They should be able to run the app with 
different input parameters. It makes use of the argparse module from the standard library.

Attributes:

Methods:
    get_command_line_args():
        this function instantiates argparser
"""

def get_command_line_args():
    """this function instantiates argparser
    
    This function instantiates argparser, and gives it basic information 
    about the application. Then, it prepares the user defined options for
    the command line interface program.

    Parameters
    ----------
    none

    Returns
    -------
    the parsed command line args as a namespace/key-value pair object
    """
        
    parser = argparse.ArgumentParser(
        prog = "pycalc",
        description = "PyCalc is a simple calculator.",
    )

    parser.add_argument("-V", "--version",
        action = "version",
        version = f"%(prog)s v{__version__}"
    )
    
    return parser.parse_args()