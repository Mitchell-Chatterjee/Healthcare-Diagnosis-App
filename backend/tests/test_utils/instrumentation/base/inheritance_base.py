"""
Base class for instrumented components using DeepEval.
"""

from abc import ABC, abstractmethod
from typing import List
from deepeval.metrics import BaseMetric

from tests.test_utils.utils.evaluation_utils import component_eval_enabled


class InstrumentedBase(ABC):
    """Base class that automatically instruments run methods and enforces explicit metrics."""
    
    def __init_subclass__(cls, **kwargs):
        """Automatically instrument run method when subclass is created."""
        super().__init_subclass__(**kwargs)
        # Only instrument if this class has actually implemented observability_metrics. Ensures intermediate classes are not instrumented
        if cls._instrumentation_enabled():
            cls._instrument_run_method()

    @classmethod
    def _instrumentation_enabled(cls) -> bool:
        """Check if this class has actually implemented observability_metrics. Ensures intermediate classes are not instrumented."""
        return component_eval_enabled() and cls.observability_metrics.__name__ in cls.__dict__

    @classmethod
    @abstractmethod
    def _instrument_run_method(cls):
        """Instrument the run method for this class."""
        pass

    @classmethod
    @abstractmethod
    def observability_metrics(cls) -> List[BaseMetric]:
        """Each subclass must implement its own metrics."""
        pass
