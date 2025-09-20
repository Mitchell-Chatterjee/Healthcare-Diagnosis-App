import pytest
from backend.agents.symptom_extraction_agent.schemas import (
    SymptomExtractionRequest, 
    SymptomExtractionResponse, 
    ExtractedSymptom
)


class TestSymptomExtractionSchemas:
    """Test cases for Symptom Extraction Agent schemas."""
    
    def test_extraction_request_creation(self):
        """Test creating a symptom extraction request."""
        request = SymptomExtractionRequest(
            patient_inquiry="I've been having chest pain for 3 days",
            context="Patient is 45 years old"
        )
        assert request.patient_inquiry == "I've been having chest pain for 3 days"
        assert request.context == "Patient is 45 years old"
        
    def test_extracted_symptom_creation(self):
        """Test creating an extracted symptom."""
        symptom = ExtractedSymptom(
            symptom="chest pain",
            severity="moderate",
            duration="3 days", 
            frequency="intermittent",
            location="left chest"
        )
        assert symptom.symptom == "chest pain"
        assert symptom.duration == "3 days"
        
    def test_extraction_response_creation(self):
        """Test creating a symptom extraction response."""
        symptom = ExtractedSymptom(symptom="chest pain", severity="moderate")
        response = SymptomExtractionResponse(
            extracted_symptoms=[symptom],
            symptom_summary=["chest pain"],
            key_concerns=["cardiac evaluation needed"],
            timeline="Started 3 days ago"
        )
        assert len(response.extracted_symptoms) == 1
        assert "chest pain" in response.symptom_summary