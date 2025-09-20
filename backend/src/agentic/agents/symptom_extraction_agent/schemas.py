from pydantic import BaseModel, Field
from typing import List, Optional


class SymptomExtractionRequest(BaseModel):
    """Input schema for the Symptom Extraction Agent."""
    patient_inquiry: str = Field(..., description="The patient's health inquiry or description")
    context: Optional[str] = Field(None, description="Additional context if available")


class ExtractedSymptom(BaseModel):
    """Individual symptom schema."""
    symptom: str = Field(..., description="The symptom name/description")
    severity: Optional[str] = Field(None, description="Severity level if mentioned")
    duration: Optional[str] = Field(None, description="Duration if mentioned") 
    frequency: Optional[str] = Field(None, description="Frequency if mentioned")
    location: Optional[str] = Field(None, description="Body location if specified")


class SymptomExtractionResponse(BaseModel):
    """Output schema for the Symptom Extraction Agent."""
    extracted_symptoms: List[ExtractedSymptom] = Field(..., description="List of extracted symptoms with details")
    symptom_summary: List[str] = Field(..., description="Simple list of symptom names")
    key_concerns: List[str] = Field(..., description="Main health concerns identified")
    timeline: Optional[str] = Field(None, description="Timeline of symptom onset/progression")
    missing_information: List[str] = Field(default_factory=list, description="Information that would be helpful to clarify")