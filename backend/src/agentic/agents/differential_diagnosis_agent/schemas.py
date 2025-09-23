from pydantic import BaseModel, Field
from typing import List


class DifferentialDiagnosisRequest(BaseModel):
    """Simplified input schema for the Differential Diagnosis Agent v1."""
    patient_inquiry: str = Field(..., description="The patient's health inquiry or symptoms")


class DifferentialDiagnosisResponse(BaseModel):
    """Simplified output schema for the Differential Diagnosis Agent v1."""
    clinical_summary: str = Field(..., description="Summary of the patient's presentation")
    possible_conditions: List[str] = Field(..., description="List of possible medical conditions") 
    most_likely_condition: str = Field(..., description="Most probable condition")
    recommended_tests: List[str] = Field(..., description="Recommended diagnostic tests")
    red_flags: List[str] = Field(default_factory=list, description="Warning signs to watch for")


# Legacy compatibility
DiagnosticRequest = DifferentialDiagnosisRequest
DiagnosticResponse = DifferentialDiagnosisResponse