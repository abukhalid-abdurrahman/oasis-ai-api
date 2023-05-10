import json
from typing import Any

class Dataset():
    """
    Represents an object that contains dataset information and datapoints.
    """

    __datasetPath: str
    """
    Path to .json file, that contains a dataset.
    """

    _datasetEntry: Any
    """
    Represents a dataset entry object, that contains a raw metadata and datapoints.
    """

    _naturalLanguage: str
    """
    Represents a natural language of dataset.
    """

    _datapointsCount: int
    """
    Represents a datapoints count.
    """

    _languageName: str
    """
    Represents a programming language full name.
    """

    _languageShortName: str
    """
    Represents a programming language short name.
    """

    _datapoints: list
    """
    Represents a list of datapoints.
    """

    def __init__(self, path) -> None:
        """
        Represents a method for initialize dataset instance.
        """
        if path is None:
            raise Exception("path argument can not be None!")

        self.__datasetPath = path
        self._datapoints = []

    def __set_metadata(self, datasetEntry: Any):
        """
        Represents a method for setting up dataset metadata.
        """

        self._naturalLanguage = datasetEntry["metadata"]["naturalLanguage"]
        self._datapointsCount = datasetEntry["metadata"]["datapointsCount"]
        self._languageName = datasetEntry["metadata"]["languageName"]
        self._languageShortName = datasetEntry["metadata"]["languageShortName"]

    def __set_datapoint(self, datasetEntry: Any):
        """
        Represents a method for setting up dataset datapoints.
        """
        for item in datasetEntry["data"]:
            self._datapoints.append(item)

    def initialize(self):
        """
        Represents a method for setting up dataset.
        """

        datasetEntry = None
        with open(self.__datasetPath) as datasetFile:
            datasetEntry = json.load(datasetFile)
            self._datasetEntry = datasetEntry

        self.__set_metadata(datasetEntry)
        self.__set_datapoint(datasetEntry)