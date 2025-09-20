from pydantic import BaseModel, Field
from typing import List, Optional


class DiagnosticRequest(BaseModel):
    """Input schema for the Diagnostic Agent."""
    patient_inquiry: str = Field(..., description="The patient's original health inquiry")
    extracted_symptoms: List[str] = Field(..., description="List of extracted symptoms")
    research_findings: str = Field(..., description="Research findings from medical research")
    test_results: str = Field(..., description="Results from medical tests")
    

class DiagnosticResponse(BaseModel):
    """Output schema for the Diagnostic Agent."""
    primary_diagnosis: str = Field(..., description="Primary suspected diagnosis")
    differential_diagnoses: List[str] = Field(..., description="Alternative diagnoses to consider")
    confidence_level: str = Field(..., description="Confidence level (High/Medium/Low)")
    reasoning: str = Field(..., description="Detailed medical reasoning")
    recommendations: List[str] = Field(..., description="Next steps and recommendations")
    follow_up_needed: bool = Field(..., description="Whether follow-up is required")