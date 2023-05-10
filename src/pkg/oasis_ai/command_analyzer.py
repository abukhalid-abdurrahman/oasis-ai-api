import sys
sys.path.insert(0, 'errors')

from errors.argument_error import ArgumentError
from errors.notfound_error import NotFoundError
from initializer import Initializer

class CommandAnalyzer():
    """
    Represents a command analyzer class for processing user commands.
    """

    __initializer: Initializer
    """
    Represents an Initializer thread-safe, singleton instance.
    """

    __similarity_rate: float
    """
    Represents a rate of similarity.
    """

    def __init__(self) -> None:
        """
        Represents a constructor for creating CommandAnalyzer instance.
        """

        self.__similarity_rate = 0.55
        self.__initializer = Initializer()
        self.__initializer.initialize()

    def execute_command(self, command: str):
        """
        Represents a command executor method, for checking command and queries similarity.
        """
        
        if command is None or len(command) <= 0:
            raise ArgumentError("command")
        
        docable_cmd = self.__initializer._nlp(command)

        for item in self.__initializer._tokenized_datapoints:
            tokenized_query = item['query']

            similarity = docable_cmd.similarity(tokenized_query)

            if(similarity >= self.__similarity_rate):
                return item
        
        raise NotFoundError("tokenized_query")
