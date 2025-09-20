"""
Common medical data structures and schemas used across the Healthcare Diagnosis App.
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class SeverityLevel(str, Enum):
    """Medical severity levels."""
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    CRITICAL = "critical"


class UrgencyLevel(str, Enum):
    """Medical urgency levels."""
    ROUTINE = "routine"
    URGENT = "urgent"
    EMERGENCY = "emergency"


class ConfidenceLevel(str, Enum):
    """Confidence levels for medical assessments."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TestStatus(str, Enum):
    """Medical test result status."""
    NORMAL = "normal"
    ABNORMAL = "abnormal"  
    CRITICAL = "critical"
    INCONCLUSIVE = "inconclusive"


class Symptom(BaseModel):
    """Standardized symptom representation."""
    name: str = Field(..., description="The symptom name")
    severity: Optional[SeverityLevel] = Field(None, description="Severity level")
    duration: Optional[str] = Field(None, description="How long symptom has persisted")
    frequency: Optional[str] = Field(None, description="How often symptom occurs")
    location: Optional[str] = Field(None, description="Body location if applicable")
    description: Optional[str] = Field(None, description="Additional details")
    onset: Optional[str] = Field(None, description="When symptom started")


class MedicalTest(BaseModel):
    """Standardized medical test representation."""
    name: str = Field(..., description="Test name")
    code: Optional[str] = Field(None, description="Medical test code (CPT, LOINC, etc.)")
    category: Optional[str] = Field(None, description="Test category")
    description: Optional[str] = Field(None, description="Test description")


class TestResult(BaseModel):
    """Standardized test result representation."""
    test: MedicalTest = Field(..., description="The test that was performed")
    value: str = Field(..., description="Test result value")
    unit: Optional[str] = Field(None, description="Unit of measurement")
    reference_range: Optional[str] = Field(None, description="Normal reference range")
    status: TestStatus = Field(..., description="Result status")
    flags: List[str] = Field(default_factory=list, description="Result flags (H, L, etc.)")
    interpretation: Optional[str] = Field(None, description="Clinical interpretation")
    timestamp: Optional[datetime] = Field(None, description="When test was performed")


class Diagnosis(BaseModel):
    """Standardized diagnosis representation."""
    condition: str = Field(..., description="Diagnosed condition")
    icd_code: Optional[str] = Field(None, description="ICD-10 code")
    confidence: ConfidenceLevel = Field(..., description="Confidence in diagnosis")
    severity: Optional[SeverityLevel] = Field(None, description="Condition severity")
    reasoning: str = Field(..., description="Medical reasoning")
    supporting_evidence: List[str] = Field(default_factory=list, description="Evidence supporting diagnosis")


class MedicalRecommendation(BaseModel):
    """Standardized medical recommendation."""
    type: str = Field(..., description="Recommendation type (test, treatment, referral, etc.)")
    description: str = Field(..., description="Recommendation description")
    urgency: UrgencyLevel = Field(..., description="Recommendation urgency")
    reasoning: Optional[str] = Field(None, description="Reason for recommendation")
    follow_up_timeline: Optional[str] = Field(None, description="When to follow up")


class DiagnosticSession(BaseModel):
    """Complete diagnostic session data."""
    session_id: str = Field(..., description="Unique session identifier")
    patient_inquiry: str = Field(..., description="Original patient inquiry")
    extracted_symptoms: List[Symptom] = Field(..., description="Identified symptoms")
    performed_tests: List[TestResult] = Field(default_factory=list, description="Tests performed")
    research_findings: Optional[str] = Field(None, description="Research summary")
    primary_diagnosis: Optional[Diagnosis] = Field(None, description="Primary diagnosis")
    differential_diagnoses: List[Diagnosis] = Field(default_factory=list, description="Alternative diagnoses")
    recommendations: List[MedicalRecommendation] = Field(default_factory=list, description="Medical recommendations")
    session_status: str = Field(..., description="Session status")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Session creation time")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update time")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional session metadata")