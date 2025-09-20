from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum


class VINDICATEMCategory(str, Enum):
    """VINDICATEM mnemonic categories for systematic differential diagnosis."""
    VASCULAR = "vascular"
    INFLAMMATORY_INFECTIOUS = "inflammatory_infectious" 
    NEOPLASTIC = "neoplastic"
    DEGENERATIVE_DEFICIENCY_DRUGS = "degenerative_deficiency_drugs"
    IDIOPATHIC_INTOXICATION_IATROGENIC = "idiopathic_intoxication_iatrogenic"
    CONGENITAL = "congenital"
    AUTOIMMUNE_ALLERGIC_ANATOMIC = "autoimmune_allergic_anatomic"
    TRAUMATIC = "traumatic"
    ENDOCRINE_ENVIRONMENTAL = "endocrine_environmental"
    METABOLIC = "metabolic"


class RiskLevel(str, Enum):
    """Risk stratification levels."""
    EMERGENT = "emergent"  # Immediate life-threatening
    URGENT = "urgent"      # Requires prompt attention
    ROUTINE = "routine"    # Standard follow-up
    LOW_RISK = "low_risk"  # Minimal immediate concern


class ProbabilityLevel(str, Enum):
    """Probability assessment levels."""
    VERY_HIGH = "very_high"    # >80%
    HIGH = "high"              # 60-80%
    MODERATE = "moderate"      # 30-60%
    LOW = "low"                # 10-30%
    VERY_LOW = "very_low"      # <10%


class DifferentialDiagnosisRequest(BaseModel):
    """Input schema for the Differential Diagnosis Agent."""
    patient_inquiry: str = Field(..., description="The patient's original health inquiry or clinical presentation")
    medical_history: Optional[str] = Field(None, description="Relevant past medical history")
    family_history: Optional[str] = Field(None, description="Relevant family medical history")
    current_medications: Optional[List[str]] = Field(None, description="Current medications and dosages")
    allergies: Optional[List[str]] = Field(None, description="Known allergies and adverse reactions")
    social_history: Optional[str] = Field(None, description="Relevant social history (smoking, alcohol, etc.)")
    physical_exam_findings: Optional[str] = Field(None, description="Physical examination findings if available")
    vital_signs: Optional[Dict[str, str]] = Field(None, description="Vital signs if available")
    laboratory_results: Optional[str] = Field(None, description="Laboratory test results")
    imaging_results: Optional[str] = Field(None, description="Imaging study results")


class CandidateCondition(BaseModel):
    """Individual candidate condition in differential diagnosis."""
    condition_name: str = Field(..., description="Name of the condition")
    vindicatem_category: VINDICATEMCategory = Field(..., description="VINDICATEM category classification")
    probability: ProbabilityLevel = Field(..., description="Estimated probability of this condition")
    risk_level: RiskLevel = Field(..., description="Risk level if condition is missed")
    supporting_evidence: List[str] = Field(..., description="Clinical findings that support this diagnosis")
    contradicting_evidence: Optional[List[str]] = Field(None, description="Findings that argue against this diagnosis")
    reasoning: str = Field(..., description="Clinical reasoning for including this condition")


class DiagnosticTest(BaseModel):
    """Recommended diagnostic test."""
    test_name: str = Field(..., description="Name of the diagnostic test")
    rationale: str = Field(..., description="Why this test is recommended")
    priority: RiskLevel = Field(..., description="Priority level for this test")
    target_conditions: List[str] = Field(..., description="Conditions this test helps rule in/out")


class DifferentialDiagnosisResponse(BaseModel):
    """Output schema for the Differential Diagnosis Agent following clinical methodology."""
    
    # Step 1: Clinical Summary
    clinical_summary: str = Field(..., description="Concise summary of key clinical findings and presentation")
    
    # Step 2: Differential Diagnoses (prioritized)
    differential_diagnoses: List[CandidateCondition] = Field(
        ..., 
        description="Prioritized list of candidate conditions using VINDICATEM systematic approach"
    )
    
    # Step 3: Risk Stratification  
    most_likely_diagnosis: str = Field(..., description="Most probable diagnosis based on clinical evidence")
    must_not_miss_diagnoses: List[str] = Field(
        ..., 
        description="High-risk conditions that must be ruled out even if less likely"
    )
    
    # Step 4: Diagnostic Recommendations
    recommended_tests: List[DiagnosticTest] = Field(..., description="Recommended diagnostic tests with rationale")
    immediate_actions: Optional[List[str]] = Field(None, description="Immediate actions required for high-risk scenarios")
    
    # Additional Clinical Guidance
    patient_education_points: List[str] = Field(..., description="Key points for patient understanding")
    follow_up_recommendations: str = Field(..., description="Recommended follow-up timeline and plan")
    red_flag_symptoms: List[str] = Field(..., description="Warning symptoms that require immediate medical attention")
    specialist_referral: Optional[str] = Field(None, description="Recommended specialist referral if indicated")
    
    # Professional Disclaimers
    medical_disclaimer: str = Field(
        default="This analysis is for educational purposes only. Always consult with qualified healthcare professionals for medical diagnosis and treatment decisions.",
        description="Medical disclaimer and limitations"
    )
    confidence_assessment: str = Field(..., description="Overall confidence in the differential diagnosis analysis")
    missing_information: Optional[List[str]] = Field(None, description="Critical information needed for more accurate diagnosis")


# Legacy compatibility
DiagnosticRequest = DifferentialDiagnosisRequest
DiagnosticResponse = DifferentialDiagnosisResponse