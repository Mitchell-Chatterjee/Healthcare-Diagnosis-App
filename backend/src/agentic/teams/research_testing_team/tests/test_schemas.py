import pytest
from backend.src.agentic.teams.research_testing_team.schemas import (
    ResearchTestingRequest,
    ResearchTestingResponse,
    ResearchPhaseResult,
    TestingPhaseResult
)


class TestResearchTestingSchemas:
    """Test cases for Research Testing Team schemas."""
    
    def test_research_testing_request_creation(self):
        """Test creating a research testing request."""
        request = ResearchTestingRequest(
            patient_inquiry="I have chest pain and shortness of breath",
            context="45-year-old male, history of hypertension"
        )
        assert request.patient_inquiry == "I have chest pain and shortness of breath"
        assert "hypertension" in request.context
        
    def test_research_phase_result_creation(self):
        """Test creating a research phase result."""
        result = ResearchPhaseResult(
            research_summary="Symptoms suggest possible cardiac condition",
            possible_conditions=["Myocardial infarction", "Angina"],
            recommended_tests=["ECG", "Troponin", "Chest X-ray"],
            urgency_assessment="Urgent"
        )
        assert result.urgency_assessment == "Urgent"
        assert len(result.recommended_tests) == 3
        
    def test_testing_phase_result_creation(self):
        """Test creating a testing phase result."""
        result = TestingPhaseResult(
            tests_performed=["ECG", "Troponin I"],
            test_results="ECG normal, Troponin elevated at 0.15 ng/mL",
            test_reasoning="Chest pain requires cardiac evaluation"
        )
        assert len(result.tests_performed) == 2
        assert "elevated" in result.test_results
        
    def test_research_testing_response_creation(self):
        """Test creating a complete research testing response."""
        research_result = ResearchPhaseResult(
            research_summary="Cardiac workup indicated",
            possible_conditions=["MI"],
            recommended_tests=["ECG"],
            urgency_assessment="Urgent"
        )
        testing_result = TestingPhaseResult(
            tests_performed=["ECG"],
            test_results="Abnormal",
            test_reasoning="Chest pain protocol"
        )
        
        response = ResearchTestingResponse(
            original_patient_inquiry="Chest pain",
            extracted_symptoms=["chest pain"],
            research_findings=research_result,
            test_results=testing_result,
            completion_status="Complete"
        )
        
        assert response.completion_status == "Complete"
        assert response.iteration_count == 1