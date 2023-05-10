class NotFoundError(Exception):
    """
    Represents an exception, that indicates unfounded resource.

    Note: Raise/Use if some resource is not found.
    """
    
    def __init__(self, argumentName) -> None:
        super().__init__(f'Resource, named as {argumentName}, not found!')