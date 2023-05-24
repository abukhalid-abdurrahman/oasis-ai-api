import spacy

from threading import Lock

from globalization_pool import GlobalizationPool
from globalization_data import EnglishCSharpGlobalizationData
from spacy.language import Language

class InitializerMeta(type):
    """
    Represents a meta class for a thread safe Initializer instance.
    """
    
    _instances = {}
    """
    Stores instaces of thread safe Initializer class.
    """
    
    _lock: Lock = Lock()
    """
    A lock object will be used to synchronize threads during
    first access to the Initializer.
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

class Initializer(metaclass=InitializerMeta):
    """
    Represents an Initializer class, for initializing: nlp, globalization pool, datasets, docable dataset
    """

    _tokenized_datapoints: list
    """
    Represents a tokenized datapoints.
    """

    _nlp: Language
    """
    Represents a NLP processor.
    """
    
    _globalizationPool: GlobalizationPool
    """
    Represents a globalization pool, for storing globalozation data.
    """

    def __init__(self) -> None:
        """
        Represents a constructor for creating an Initializer thread safe, singleton instance.
        """

        self._tokenized_datapoints = []

    def initialize(self):
        self.__initialize_nlp()
        self.__initialize_pool()
        self.__initialize_globalization_data()
        self.__tokenize_oasis_dataset()

    def __initialize_nlp(self):
        """
        Represents an initializer method for NLP processor.
        """
        
        self._nlp = spacy.load("en_core_web_md")
    
    def __initialize_pool(self):
        """
        Represents an initializer method for GlobalizationPool.
        """
        
        self._globalizationPool = GlobalizationPool()

    def __initialize_globalization_data(self):
        """
        Represents an initializer method for GlobalizationData.
        """
        
        englishCsharpData = EnglishCSharpGlobalizationData()
        
        self._globalizationPool.store(englishCsharpData)

    def __tokenize_oasis_dataset(self):
        """
        Represents an initializer method for OASIS Dataset.
        """
        
        englishCsharpData = self._globalizationPool.get(plang="csharp", nlang="en-US")

        for datapoint in englishCsharpData._dataset._datapoints:
            query = datapoint['query']
            source = datapoint['source']
            partially = datapoint['partially']
            params = datapoint['params']

            doc = self._nlp(query)

            docable_datapoint = \
                { 'query': doc, 'source': source, 'partially': partially, 'params': params  }
            
            self._tokenized_datapoints.append(docable_datapoint)