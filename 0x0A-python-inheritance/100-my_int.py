#!/usr/bin/python3

"""Module with a custom class that inherits from int class"""

class MyInt(int):
    """A subclass of int"""

    def __eq__(self, other_type):
        """Returns the inverse of `equality` operation

            Args:
                other_type (object): Object to compare the type to

            Returns:
                Inverse of the equality comparison
        """
        return super().__ne__(other_type)

    def __ne__(self, other_type):
        """Returns the inverse of the `not equal` operation

            Args:
                other_type (object): Object to compare the type to

            Returns:
                Inverse of the `non-equality` comparison
        """
        return super().__eq__(other_type)
