from .agent import DifferentialDiagnosisAgent

# Legacy compatibility
DiagnosticAgent = DifferentialDiagnosisAgent

# Only import schemas that actually exist
from .schemas import DifferentialDiagnosisRequest, DifferentialDiagnosisResponse

__all__ = ["DifferentialDiagnosisAgent", "DiagnosticAgent", "DifferentialDiagnosisRequest", "DifferentialDiagnosisResponse"]
