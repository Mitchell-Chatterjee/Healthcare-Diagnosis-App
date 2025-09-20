import pytest
from backend.agents.medical_test_agent.schemas import MedicalTestRequest, MedicalTestResponse, TestResult


class TestMedicalTestSchemas:
    """Test cases for Medical Test Agent schemas."""
    
    def test_test_request_creation(self):
        """Test creating a medical test request."""
        request = MedicalTestRequest(
            patient_inquiry="I have chest pain",
            symptoms=["chest pain", "shortness of breath"],
            research_summary="Research suggests cardiac workup needed"
        )
        assert request.patient_inquiry == "I have chest pain"
        assert len(request.symptoms) == 2
        
    def test_test_result_creation(self):
        """Test creating a test result."""
        result = TestResult(
            test_name="Troponin I",
            result_value="0.15 ng/mL",
            normal_range="< 0.04 ng/mL",
            status="Abnormal",
            clinical_significance="Elevated troponin suggests myocardial injury"
        )
        assert result.test_name == "Troponin I"
        assert result.status == "Abnormal"
        
    def test_test_response_creation(self):
        """Test creating a medical test response."""
        test_result = TestResult(
            test_name="ECG",
            result_value="Sinus rhythm",
            normal_range="Normal sinus rhythm",
            status="Normal", 
            clinical_significance="No acute changes"
        )
        response = MedicalTestResponse(
            tests_performed=["ECG", "Troponin"],
            test_results=[test_result],
            test_selection_reasoning="Chest pain requires cardiac evaluation",
            overall_findings="Mixed results require further evaluation"
        )
        assert len(response.tests_performed) == 2
        assert len(response.test_results) == 1