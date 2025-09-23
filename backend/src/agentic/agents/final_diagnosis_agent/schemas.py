from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum


class ConfidenceLevel(str, Enum):
    """Confidence levels for final diagnosis."""
    VERY_HIGH = "very_high"    # >90% confident
    HIGH = "high"              # 75-90% confident  
    MODERATE = "moderate"      # 50-75% confident
    LOW = "low"                # 25-50% confident
    VERY_LOW = "very_low"      # <25% confident


class DiagnosisStatus(str, Enum):
    """Status of the final diagnosis."""
    DEFINITIVE = "definitive"     # Clear diagnosis based on evidence
    PROBABLE = "probable"         # Most likely diagnosis but some uncertainty
    POSSIBLE = "possible"         # Diagnosis possible but needs more testing
    INCONCLUSIVE = "inconclusive" # Insufficient evidence for diagnosis
    REQUIRES_REFERRAL = "requires_referral"  # Needs specialist evaluation


class FinalDiagnosisRequest(BaseModel):
    """Input schema aggregating information from all previous workflow steps."""
    
    # From differential diagnosis step (which now includes symptom extraction)
    clinical_summary: Optional[str] = Field(None, description="Clinical summary including extracted symptoms")
    differential_candidates: Optional[List[Dict[str, Any]]] = Field(None, description="Differential diagnosis candidates")
    must_not_miss_conditions: Optional[List[str]] = Field(None, description="High-risk conditions to rule out")
    recommended_tests: Optional[List[Dict[str, Any]]] = Field(None, description="Recommended diagnostic tests")
    
    # From research and testing team
    research_findings: Optional[Dict[str, Any]] = Field(None, description="Research evidence and context")
    test_results: Optional[Dict[str, Any]] = Field(None, description="Actual test results if available")
    additional_evidence: Optional[str] = Field(None, description="Additional supporting evidence")
    
    # Patient context
    patient_inquiry: str = Field(..., description="Original patient inquiry")
    patient_demographics: Optional[Dict[str, str]] = Field(None, description="Age, sex, relevant demographics")
    medical_history: Optional[str] = Field(None, description="Relevant medical history")


class TreatmentRecommendation(BaseModel):
    """Treatment or management recommendation."""
    recommendation: str = Field(..., description="Specific treatment or management step")
    priority: str = Field(..., description="Priority level (immediate, urgent, routine)")
    rationale: str = Field(..., description="Reasoning for this recommendation")


class FollowUpPlan(BaseModel):
    """Follow-up planning details."""
    timeline: str = Field(..., description="When to follow up")
    what_to_monitor: List[str] = Field(..., description="Symptoms or parameters to monitor")
    when_to_seek_care: List[str] = Field(..., description="Red flag symptoms requiring immediate care")


class FinalDiagnosisResponse(BaseModel):
    """Output schema for the Final Diagnosis Agent with comprehensive educational disclaimers."""
    
    # MANDATORY EDUCATIONAL DISCLAIMER
    educational_disclaimer: str = Field(
        default="🎓 EDUCATIONAL CONTENT ONLY: This analysis is created for educational and informational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare professionals for medical concerns. Never disregard professional medical advice or delay seeking treatment based on this educational content.",
        description="Mandatory educational disclaimer prominently displayed"
    )
    
    # Final diagnosis synthesis
    final_diagnosis: str = Field(..., description="The concluded most likely diagnosis based on all available evidence")
    diagnosis_status: DiagnosisStatus = Field(..., description="Status/certainty level of the diagnosis")
    confidence_level: ConfidenceLevel = Field(..., description="Confidence in the final diagnosis")
    
    # Evidence synthesis
    supporting_evidence: List[str] = Field(..., description="Key evidence supporting the final diagnosis")
    alternative_diagnoses: Optional[List[str]] = Field(None, description="Other possible diagnoses still under consideration")
    ruled_out_conditions: List[str] = Field(..., description="Conditions successfully ruled out by evidence/testing")
    
    # Clinical reasoning
    diagnostic_reasoning: str = Field(..., description="Detailed explanation of how the diagnosis was reached")
    key_clinical_factors: List[str] = Field(..., description="Most important clinical factors in the diagnosis")
    
    # Actionable recommendations
    immediate_actions: Optional[List[str]] = Field(None, description="Actions needed immediately")
    treatment_recommendations: Optional[List[TreatmentRecommendation]] = Field(None, description="Treatment/management recommendations")
    lifestyle_modifications: Optional[List[str]] = Field(None, description="Lifestyle changes that may help")
    
    # Follow-up planning
    follow_up_plan: FollowUpPlan = Field(..., description="Follow-up and monitoring plan")
    specialist_referral: Optional[str] = Field(None, description="Specialist referral if recommended")
    additional_testing: Optional[List[str]] = Field(None, description="Additional tests that may be helpful")
    
    # Safety and limitations
    red_flag_warnings: List[str] = Field(..., description="Warning signs that require immediate medical attention")
    limitations_noted: List[str] = Field(..., description="Limitations in the current analysis")
    missing_information: Optional[List[str]] = Field(None, description="Important information that would improve diagnosis accuracy")
    
    # Quality metrics
    evidence_quality: str = Field(..., description="Assessment of the quality and completeness of available evidence")
    diagnostic_certainty: str = Field(..., description="Overall certainty and any remaining diagnostic uncertainty")
    
    # Additional educational content
    condition_education: Optional[str] = Field(None, description="Educational information about the diagnosed condition")
    prevention_tips: Optional[List[str]] = Field(None, description="Prevention tips related to the condition")


# Legacy compatibility if needed
DiagnosticSynthesisRequest = FinalDiagnosisRequest  
DiagnosticSynthesisResponse = FinalDiagnosisResponse