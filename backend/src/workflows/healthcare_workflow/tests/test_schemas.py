import pytest
from backend.workflows.healthcare_workflow.schemas import (
    HealthcareWorkflowRequest,
    HealthcareWorkflowResponse,
    WorkflowStepResult
)


class TestHealthcareWorkflowSchemas:
    """Test cases for Healthcare Workflow schemas."""
    
    def test_workflow_request_creation(self):
        """Test creating a workflow request."""
        request = HealthcareWorkflowRequest(
            patient_inquiry="I have chest pain and shortness of breath",
            patient_context="45-year-old male, smoker, family history of heart disease",
            session_id="session_123"
        )
        assert request.patient_inquiry == "I have chest pain and shortness of breath"
        assert request.session_id == "session_123"
        
    def test_workflow_step_result_creation(self):
        """Test creating a workflow step result."""
        result = WorkflowStepResult(
            step_name="Symptom Extraction Step",
            step_type="agent",
            execution_time=2.5,
            result_content="Extracted symptoms: chest pain, shortness of breath",
            metadata={"agent_name": "SymptomExtractionAgent"},
            success=True
        )
        assert result.step_name == "Symptom Extraction Step"
        assert result.success is True
        assert result.execution_time == 2.5
        
    def test_workflow_response_creation(self):
        """Test creating a complete workflow response."""
        symptom_step = WorkflowStepResult(
            step_name="Symptom Extraction",
            step_type="agent",
            result_content="Symptoms extracted",
            success=True
        )
        research_step = WorkflowStepResult(
            step_name="Research Testing", 
            step_type="team",
            result_content="Research and tests completed",
            success=True
        )
        diagnostic_step = WorkflowStepResult(
            step_name="Diagnostic Analysis",
            step_type="agent", 
            result_content="Diagnosis provided",
            success=True
        )
        
        response = HealthcareWorkflowResponse(
            session_id="session_123",
            original_inquiry="Chest pain",
            symptom_extraction_result=symptom_step,
            research_testing_result=research_step,
            diagnostic_result=diagnostic_step,
            final_diagnosis="Possible myocardial infarction",
            extracted_symptoms=["chest pain", "shortness of breath"],
            tests_performed=["ECG", "Troponin"],
            research_findings="Cardiac condition suspected",
            recommendations=["Emergency evaluation", "Cardiology consult"],
            workflow_status="Success",
            confidence_score=0.85
        )
        
        assert response.session_id == "session_123"
        assert response.workflow_status == "Success"
        assert response.confidence_score == 0.85
        assert len(response.recommendations) == 2