from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """
    Base class for all analyzers.
    """

    @abstractmethod
    def analyze(self, file_path: str) -> dict:
        """
        Analyze a Python file and return the analysis result.
        """
        pass