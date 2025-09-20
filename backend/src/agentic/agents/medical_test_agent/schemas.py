from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class MedicalTestRequest(BaseModel):
    """Input schema for the Medical Test Agent."""
    patient_inquiry: str = Field(..., description="The patient's original health inquiry")
    symptoms: List[str] = Field(..., description="List of extracted symptoms")
    research_summary: str = Field(..., description="Research findings and recommendations")


class TestResult(BaseModel):
    """Individual test result schema."""
    test_name: str = Field(..., description="Name of the test performed")
    result_value: str = Field(..., description="Test result value")
    normal_range: str = Field(..., description="Normal reference range")
    status: str = Field(..., description="Normal/Abnormal/Critical")
    clinical_significance: str = Field(..., description="Clinical interpretation")


class MedicalTestResponse(BaseModel):
    """Output schema for the Medical Test Agent."""
    tests_performed: List[str] = Field(..., description="List of tests that were executed")
    test_results: List[TestResult] = Field(..., description="Detailed test results")
    test_selection_reasoning: str = Field(..., description="Reasoning for test selection")
    additional_tests_suggested: List[str] = Field(default_factory=list, description="Additional recommended tests")
    overall_findings: str = Field(..., description="Summary of all test findings")