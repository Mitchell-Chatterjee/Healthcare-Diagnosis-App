from pydantic import BaseModel, Field
from typing import List, Optional


class MedicalResearchRequest(BaseModel):
    """Input schema for the Medical Research Agent."""
    patient_inquiry: str = Field(..., description="The patient's health inquiry")
    symptoms: List[str] = Field(..., description="List of extracted symptoms")
    search_query: Optional[str] = Field(None, description="Specific search query if provided")


class MedicalResearchResponse(BaseModel):
    """Output schema for the Medical Research Agent."""
    research_summary: str = Field(..., description="Summary of research findings")
    possible_conditions: List[str] = Field(..., description="Possible medical conditions identified")
    recommended_tests: List[str] = Field(..., description="Tests recommended based on research")
    search_sources: List[str] = Field(..., description="Sources used in research")
    urgency_level: str = Field(..., description="Urgency assessment (Urgent/Moderate/Routine)")
    additional_questions: List[str] = Field(default_factory=list, description="Questions for clarification")