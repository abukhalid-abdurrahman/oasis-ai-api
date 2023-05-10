from dataset import Dataset

class GlobalizationData():
    """
    Represents a base globalization object.
    """
    
    _lang: str
    """
    Represents a natural language of dataset.
    """
    
    _dataset: Dataset
    """
    Represents a dataset.
    """

class EnglishCSharpGlobalizationData(GlobalizationData):
    """
    Represents an English language globalization object.
    """
    
    def __init__(self) -> None:
        """
        Represents a method for initializing a globalization object.
        """
        self._lang = "en-US"
        self._dataset = Dataset("csharp_data_en.json")

        self._dataset.initialize()