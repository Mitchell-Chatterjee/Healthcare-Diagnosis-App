import pytest
from backend.src.agentic.agents.diagnostic_agent.schemas import DiagnosticRequest, DiagnosticResponse


class TestDiagnosticSchemas:
    """Test cases for Diagnostic Agent schemas."""
    
    def test_diagnostic_request_creation(self):
        """Test creating a diagnostic request."""
        request = DiagnosticRequest(
            patient_inquiry="I have chest pain",
            extracted_symptoms=["chest pain", "shortness of breath"],
            research_findings="Possible cardiac condition",
            test_results="ECG shows abnormal rhythm"
        )
        assert request.patient_inquiry == "I have chest pain"
        assert len(request.extracted_symptoms) == 2
        
    def test_diagnostic_response_creation(self):
        """Test creating a diagnostic response."""
        response = DiagnosticResponse(
            primary_diagnosis="Atrial fibrillation",
            differential_diagnoses=["Anxiety", "GERD"],
            confidence_level="High",
            reasoning="ECG shows irregular rhythm consistent with AFib",
            recommendations=["Cardiology consultation", "Blood thinners"],
            follow_up_needed=True
        )
        assert response.primary_diagnosis == "Atrial fibrillation"
        assert response.follow_up_needed is True