from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class HealthcareWorkflowRequest(BaseModel):
    """Input schema for the Healthcare Workflow."""
    patient_inquiry: str = Field(..., description="The patient's health inquiry")
    patient_context: Optional[str] = Field(None, description="Additional patient context")
    session_id: Optional[str] = Field(None, description="Session identifier for tracking")


class WorkflowStepResult(BaseModel):
    """Result from an individual workflow step."""
    step_name: str = Field(..., description="Name of the workflow step")
    step_type: str = Field(..., description="Type: agent/team/custom")
    execution_time: Optional[float] = Field(None, description="Execution time in seconds")
    result_content: str = Field(..., description="Main content from the step")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    success: bool = Field(default=True, description="Whether the step executed successfully")
    error_message: Optional[str] = Field(None, description="Error message if step failed")


class HealthcareWorkflowResponse(BaseModel):
    """Output schema for the Healthcare Workflow."""
    session_id: str = Field(..., description="Session identifier")
    original_inquiry: str = Field(..., description="The original patient inquiry")
    
    # Step-by-step results
    symptom_extraction_result: WorkflowStepResult = Field(..., description="Results from symptom extraction")
    research_testing_result: WorkflowStepResult = Field(..., description="Results from research and testing")
    diagnostic_result: WorkflowStepResult = Field(..., description="Results from diagnostic analysis")
    
    # Final consolidated output
    final_diagnosis: str = Field(..., description="Final diagnostic conclusion")
    extracted_symptoms: List[str] = Field(..., description="All symptoms identified")
    tests_performed: List[str] = Field(..., description="All tests that were executed")
    research_findings: str = Field(..., description="Summary of research findings")
    recommendations: List[str] = Field(..., description="Final recommendations")
    
    # Workflow metadata
    total_execution_time: Optional[float] = Field(None, description="Total workflow execution time")
    workflow_status: str = Field(..., description="Status: Success/Failed/Partial")
    confidence_score: Optional[float] = Field(None, description="Overall confidence in results")
    
    # Quality and safety
    safety_flags: List[str] = Field(default_factory=list, description="Any safety concerns identified")
    quality_metrics: Dict[str, Any] = Field(default_factory=dict, description="Quality assessment metrics")