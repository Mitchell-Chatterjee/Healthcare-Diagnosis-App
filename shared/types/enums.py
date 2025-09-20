"""
Enumerated values used across the Healthcare Diagnosis App.
"""
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


class SessionStatus(str, Enum):
    """Diagnostic session status."""
    INITIALIZED = "initialized"
    IN_PROGRESS = "in_progress"
    SYMPTOM_EXTRACTION = "symptom_extraction"
    RESEARCH_PHASE = "research_phase"
    TESTING_PHASE = "testing_phase"
    DIAGNOSIS_PHASE = "diagnosis_phase"
    COMPLETED = "completed"
    FAILED = "failed"
    TIMEOUT = "timeout"


class AgentType(str, Enum):
    """Types of healthcare agents."""
    SYMPTOM_EXTRACTION = "symptom_extraction"
    MEDICAL_RESEARCH = "medical_research"
    MEDICAL_TEST = "medical_test"
    DIAGNOSTIC = "diagnostic"


class TeamType(str, Enum):
    """Types of healthcare teams."""
    RESEARCH_TESTING = "research_testing"


class WorkflowType(str, Enum):
    """Types of healthcare workflows."""
    HEALTHCARE_DIAGNOSIS = "healthcare_diagnosis"


class TestStatus(str, Enum):
    """Medical test result status."""
    NORMAL = "normal"
    ABNORMAL = "abnormal"
    CRITICAL = "critical"
    INCONCLUSIVE = "inconclusive"
    PENDING = "pending"
    CANCELLED = "cancelled"


class TestCategory(str, Enum):
    """Categories of medical tests."""
    BLOOD_WORK = "blood_work"
    IMAGING = "imaging" 
    CARDIAC = "cardiac"
    RESPIRATORY = "respiratory"
    NEUROLOGICAL = "neurological"
    GASTROINTESTINAL = "gastrointestinal"
    UROLOGICAL = "urological"
    ENDOCRINE = "endocrine"
    INFECTIOUS_DISEASE = "infectious_disease"
    OTHER = "other"


class DiagnosisType(str, Enum):
    """Types of diagnoses."""
    PRIMARY = "primary"
    DIFFERENTIAL = "differential"
    RULE_OUT = "rule_out"
    PROVISIONAL = "provisional"
    CONFIRMED = "confirmed"


class RecommendationType(str, Enum):
    """Types of medical recommendations."""
    ADDITIONAL_TESTING = "additional_testing"
    SPECIALIST_REFERRAL = "specialist_referral"
    TREATMENT = "treatment"
    LIFESTYLE_CHANGE = "lifestyle_change"
    FOLLOW_UP = "follow_up"
    EMERGENCY_CARE = "emergency_care"
    MEDICATION = "medication"
    MONITORING = "monitoring"


class SymptomType(str, Enum):
    """Types of symptoms."""
    PHYSICAL = "physical"
    EMOTIONAL = "emotional"
    COGNITIVE = "cognitive"
    BEHAVIORAL = "behavioral"


class Gender(str, Enum):
    """Gender options."""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class BloodType(str, Enum):
    """Blood type options."""
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    UNKNOWN = "unknown"


class AllergyType(str, Enum):
    """Types of allergies."""
    MEDICATION = "medication"
    FOOD = "food"
    ENVIRONMENTAL = "environmental"
    CONTACT = "contact"
    OTHER = "other"


class MedicalSpecialty(str, Enum):
    """Medical specialties for referrals."""
    CARDIOLOGY = "cardiology"
    DERMATOLOGY = "dermatology"
    ENDOCRINOLOGY = "endocrinology"
    GASTROENTEROLOGY = "gastroenterology"
    NEUROLOGY = "neurology"
    ONCOLOGY = "oncology"
    ORTHOPEDICS = "orthopedics"
    PSYCHIATRY = "psychiatry"
    PULMONOLOGY = "pulmonology"
    UROLOGY = "urology"
    EMERGENCY_MEDICINE = "emergency_medicine"
    FAMILY_MEDICINE = "family_medicine"
    INTERNAL_MEDICINE = "internal_medicine"
    PEDIATRICS = "pediatrics"


class ErrorCode(str, Enum):
    """System error codes."""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    TIMEOUT_ERROR = "TIMEOUT_ERROR"
    AGENT_ERROR = "AGENT_ERROR"
    WORKFLOW_ERROR = "WORKFLOW_ERROR"
    API_ERROR = "API_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    PERMISSION_ERROR = "PERMISSION_ERROR"
    RATE_LIMIT_ERROR = "RATE_LIMIT_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"


class LogLevel(str, Enum):
    """Logging levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"