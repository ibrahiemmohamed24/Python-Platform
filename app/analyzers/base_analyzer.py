from abc import ABC, abstractmethod

from app.domain.analysis_result import AnalysisResult


class BaseAnalyzer(ABC):
    """
    Base class for all analyzers.
    """

    @abstractmethod
    def analyze(self, file_path: str) -> AnalysisResult:
        """
        Analyze a Python file and return the analysis result.
        """
        pass