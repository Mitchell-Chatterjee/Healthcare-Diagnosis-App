from pydantic import BaseModel, Field
from typing import List, Optional
from ...agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse


class ResearchTestingRequest(BaseModel):
    """Input schema for the Research Testing Team."""
    original_inquiry: str = Field(..., description="The original patient inquiry")
    differential_diagnosis: DifferentialDiagnosisResponse = Field(
        ..., 
        description="Differential diagnosis results to research and test"
    )


class ResearchFinding(BaseModel):
    """Individual research finding from medical literature or sources."""
    topic: str = Field(..., description="Research topic or condition investigated")
    summary: str = Field(..., description="Summary of research findings")
    sources: List[str] = Field(default_factory=list, description="Research sources consulted")
    relevance: str = Field(..., description="Relevance to the patient case")


class TestResult(BaseModel):
    """Individual test result."""
    test_name: str = Field(..., description="Name of the diagnostic test")
    result: str = Field(..., description="Test result or findings")
    normal_range: Optional[str] = Field(None, description="Normal range for reference")
    interpretation: Optional[str] = Field(None, description="Clinical interpretation if available")


class ResearchTestingResponse(BaseModel):
    """Output schema for the Research Testing Team."""
    original_inquiry: str = Field(..., description="The original patient inquiry")
    differential_context: DifferentialDiagnosisResponse = Field(
        ..., 
        description="Differential diagnosis context that guided the research and testing"
    )
    research_findings: List[ResearchFinding] = Field(
        default_factory=list, 
        description="Key findings from medical research"
    )
    test_results: List[TestResult] = Field(
        default_factory=list, 
        description="Results from diagnostic tests performed"
    )
    additional_observations: List[str] = Field(
        default_factory=list, 
        description="Additional findings or observations"
    )
    completion_status: str = Field(
        ..., 
        description="Status: Complete, Needs_Follow_up, or Insufficient_Data"
    )