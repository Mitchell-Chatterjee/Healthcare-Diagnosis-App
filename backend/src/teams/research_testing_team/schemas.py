from pydantic import BaseModel, Field
from typing import List, Optional


class ResearchTestingRequest(BaseModel):
    """Input schema for the Research Testing Team."""
    patient_inquiry: str = Field(..., description="The patient's health inquiry")
    context: Optional[str] = Field(None, description="Additional context if available")


class ResearchPhaseResult(BaseModel):
    """Result from the research phase."""
    research_summary: str = Field(..., description="Summary of research findings")
    possible_conditions: List[str] = Field(..., description="Possible medical conditions")
    recommended_tests: List[str] = Field(..., description="Tests recommended by research")
    urgency_assessment: str = Field(..., description="Urgency level assessment")


class TestingPhaseResult(BaseModel):
    """Result from the testing phase."""
    tests_performed: List[str] = Field(..., description="List of tests executed")
    test_results: str = Field(..., description="Consolidated test results")
    test_reasoning: str = Field(..., description="Reasoning for test selection")


class ResearchTestingResponse(BaseModel):
    """Output schema for the Research Testing Team."""
    original_patient_inquiry: str = Field(..., description="The original patient inquiry")
    extracted_symptoms: List[str] = Field(..., description="Symptoms identified from inquiry")
    research_findings: ResearchPhaseResult = Field(..., description="Results from research phase")
    test_results: TestingPhaseResult = Field(..., description="Results from testing phase")
    additional_observations: List[str] = Field(default_factory=list, description="Additional findings")
    iteration_count: int = Field(default=1, description="Number of research-test iterations performed")
    completion_status: str = Field(..., description="Status: Complete/Needs_Follow_up")