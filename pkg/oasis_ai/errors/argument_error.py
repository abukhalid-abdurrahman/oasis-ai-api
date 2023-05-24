class ArgumentError(Exception):
    """
    Represents an argument exception.

    Note: Raise/Use if bad argument was provided.
    """
    
    def __init__(self, argumentName) -> None:
        super().__init__(f'Bad argument was provided, named as {argumentName}')