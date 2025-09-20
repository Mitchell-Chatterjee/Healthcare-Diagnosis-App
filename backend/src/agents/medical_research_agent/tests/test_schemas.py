import pytest
from backend.agents.medical_research_agent.schemas import MedicalResearchRequest, MedicalResearchResponse


class TestMedicalResearchSchemas:
    """Test cases for Medical Research Agent schemas."""
    
    def test_research_request_creation(self):
        """Test creating a medical research request."""
        request = MedicalResearchRequest(
            patient_inquiry="I have chest pain and shortness of breath",
            symptoms=["chest pain", "shortness of breath", "fatigue"]
        )
        assert request.patient_inquiry == "I have chest pain and shortness of breath"
        assert len(request.symptoms) == 3
        
    def test_research_response_creation(self):
        """Test creating a medical research response."""
        response = MedicalResearchResponse(
            research_summary="Symptoms suggest possible cardiac condition",
            possible_conditions=["Myocardial infarction", "Angina", "Anxiety"],
            recommended_tests=["ECG", "Troponin", "Chest X-ray"],
            search_sources=["PubMed", "Mayo Clinic", "WebMD"],
            urgency_level="Urgent"
        )
        assert response.urgency_level == "Urgent"
        assert len(response.recommended_tests) == 3