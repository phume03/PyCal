import sys

from pycalc import cli
from pycalc import calculator

"""The container for the entry-point to the pycalc application

This is a container for the entry-point to the PyCalc application.

Attributes:
    none

Methods:
    main():
        starts the execution of the pycalc program

"""

def main():
    """starts the execution of the pycalc application

	Parameters
	----------
	none

	Returns
	-------
	none
	"""
    args = cli.get_command_line_args()
    try:
        print("Running...")
        calculator.main()
    except Exception as error:
        print(error, file = sys.stderr)
    pass

if __name__ == "__main__":
    main()
    pass