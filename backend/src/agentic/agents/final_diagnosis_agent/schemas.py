from pydantic import BaseModel, Field
from typing import List
from ...agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse
from ...teams.research_testing_team.schemas import ResearchTestingResponse


class FinalDiagnosisRequest(BaseModel):
    """Simplified input schema for the Final Diagnosis Agent v1."""
    original_inquiry: str = Field(..., description="The original patient inquiry")
    differential_diagnosis: DifferentialDiagnosisResponse = Field(..., description="Differential diagnosis results")
    research_testing: ResearchTestingResponse = Field(..., description="Research and testing results")


class FinalDiagnosisResponse(BaseModel):
    """Simplified output schema for the Final Diagnosis Agent v1."""
    final_diagnosis: str = Field(..., description="The most likely diagnosis")
    confidence: str = Field(..., description="Confidence level: High, Medium, or Low")
    reasoning: str = Field(..., description="Brief explanation of the diagnosis")
    next_steps: List[str] = Field(..., description="Recommended next steps for the patient")
    warnings: List[str] = Field(default_factory=list, description="Important warnings or red flags")


# Legacy compatibility
DiagnosticSynthesisRequest = FinalDiagnosisRequest  
DiagnosticSynthesisResponse = FinalDiagnosisResponse