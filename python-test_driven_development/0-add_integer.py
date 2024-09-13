#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats, and returns their sum as an integer.
    
    args:
		a: firts integer or float
		b: second integer or float (default is 98)

	Returns:
		The sum of a and b, casted to an integer.
  
	Raises:
		TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
