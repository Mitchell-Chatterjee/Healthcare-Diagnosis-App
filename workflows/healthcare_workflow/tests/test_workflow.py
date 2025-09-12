import pytest
from agno_test.agents.healthcare.workflows.healthcare_workflow import HealthcareWorkflow


class TestHealthcareWorkflow:
    """Test cases for the Healthcare Workflow."""
    
    def test_workflow_initialization(self):
        """Test that the workflow initializes correctly."""
        workflow = HealthcareWorkflow()
        assert workflow.name == "Healthcare Workflow"
        assert len(workflow.steps) == 3
        assert workflow.storage is not None
    
    def test_workflow_without_storage(self):
        """Test workflow initialization without storage."""
        workflow = HealthcareWorkflow(use_storage=False)
        assert workflow.name == "Healthcare Workflow"
        assert workflow.storage is None
    
    def test_workflow_has_correct_steps(self):
        """Test that the workflow has the correct steps."""
        workflow = HealthcareWorkflow()
        step_names = [step.name for step in workflow.steps]
        expected_steps = [
            "Symptom Extraction Step",
            "Research and Testing Step", 
            "Diagnostic Step"
        ]
        assert step_names == expected_steps
