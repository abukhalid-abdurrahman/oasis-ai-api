from threading import Lock
from errors.notfound_error import NotFoundError

from globalization_data import GlobalizationData

class GlobalizationPoolMeta(type):
    """
    Represents a globaliation pool meta class, for managing thread-safe singleton GlobalizationPool class.
    """

    _instances = {}
    """
    Represents an instances of thread safe singleton object.
    """

    _lock: Lock = Lock()
    """
    A lock object will be used to synchronize threads during
    first access to the GlobalizationPool.
    """

    def __call__(cls, *args, **kwargs):
        """
        Represents a calling method.
        """

        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class GlobalizationPool(metaclass=GlobalizationPoolMeta):
    """
    Represents a globaliation pool, for storing datasets for different languages, and localizations.
    GlobalizationPool is thread safe and singleton type.
    """

    _pool: list
    """
    Represents a pool, for storing datasets for different languages, and localizations.
    """
    
    def __init__(self) -> None:
        """
        Represents a method for initializing GlobalizationPool instance.
        """
        
        self._pool = []

    def store(self, globalization_set: GlobalizationData) -> bool:
        """
        Represents a method for adding globalization data to globalization pool.
        """

        self._pool.append(globalization_set)
        return True
    
    def get(self, plang: str, nlang: str) -> GlobalizationData:
        """
        Represents a method for getting globalization data from globalization pool.
        plang argument means full name of programming language.
        nlang argument means natural language.
        """
        
        for globalization_set in self._pool:
            if globalization_set._dataset._languageName == plang and globalization_set._dataset._naturalLanguage == nlang:
                return globalization_set
        
        raise NotFoundError(f"plang: {plang}, nlang: {nlang}")