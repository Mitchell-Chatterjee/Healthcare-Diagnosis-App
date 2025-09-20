"""
Patient information schemas for the Healthcare Diagnosis App.
"""
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime, date
from enum import Enum


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
    OTHER = "other"


class Allergy(BaseModel):
    """Patient allergy information."""
    allergen: str = Field(..., description="The allergen")
    type: AllergyType = Field(..., description="Type of allergy")
    reaction: Optional[str] = Field(None, description="Typical reaction")
    severity: Optional[str] = Field(None, description="Reaction severity")


class Medication(BaseModel):
    """Current medication information."""
    name: str = Field(..., description="Medication name")
    dosage: Optional[str] = Field(None, description="Dosage amount")
    frequency: Optional[str] = Field(None, description="How often taken")
    indication: Optional[str] = Field(None, description="What it's for")
    start_date: Optional[date] = Field(None, description="When started")


class MedicalCondition(BaseModel):
    """Historical medical condition."""
    condition: str = Field(..., description="Medical condition")
    diagnosed_date: Optional[date] = Field(None, description="When diagnosed")
    status: Optional[str] = Field(None, description="Current status (active, resolved, etc.)")
    notes: Optional[str] = Field(None, description="Additional notes")


class EmergencyContact(BaseModel):
    """Emergency contact information."""
    name: str = Field(..., description="Contact name")
    relationship: str = Field(..., description="Relationship to patient")
    phone: str = Field(..., description="Phone number")
    email: Optional[EmailStr] = Field(None, description="Email address")


class PatientInfo(BaseModel):
    """Basic patient information."""
    patient_id: Optional[str] = Field(None, description="Unique patient identifier")
    first_name: Optional[str] = Field(None, description="Patient first name")
    last_name: Optional[str] = Field(None, description="Patient last name")
    date_of_birth: Optional[date] = Field(None, description="Date of birth")
    gender: Optional[Gender] = Field(None, description="Gender")
    email: Optional[EmailStr] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    
    # Medical information
    blood_type: Optional[BloodType] = Field(None, description="Blood type")
    height: Optional[str] = Field(None, description="Height")
    weight: Optional[str] = Field(None, description="Weight")
    
    # Contact information
    emergency_contact: Optional[EmergencyContact] = Field(None, description="Emergency contact")
    
    # Privacy and consent
    consent_given: bool = Field(default=False, description="Whether consent was given")
    privacy_acknowledged: bool = Field(default=False, description="Privacy policy acknowledged")


class MedicalHistory(BaseModel):
    """Patient medical history."""
    patient_id: str = Field(..., description="Patient identifier")
    
    # Current health status
    current_medications: List[Medication] = Field(default_factory=list, description="Current medications")
    allergies: List[Allergy] = Field(default_factory=list, description="Known allergies")
    
    # Medical history
    medical_conditions: List[MedicalCondition] = Field(default_factory=list, description="Past/current conditions")
    surgical_history: List[str] = Field(default_factory=list, description="Previous surgeries")
    family_history: List[str] = Field(default_factory=list, description="Family medical history")
    
    # Lifestyle factors
    smoking_status: Optional[str] = Field(None, description="Smoking status")
    alcohol_use: Optional[str] = Field(None, description="Alcohol consumption")
    exercise_frequency: Optional[str] = Field(None, description="Exercise habits")
    
    # Additional notes
    notes: Optional[str] = Field(None, description="Additional medical history notes")
    
    # Metadata
    last_updated: datetime = Field(default_factory=datetime.utcnow, description="Last update time")


class PatientSession(BaseModel):
    """Patient session context for diagnosis."""
    session_id: str = Field(..., description="Unique session identifier")
    patient_info: Optional[PatientInfo] = Field(None, description="Patient demographics")
    medical_history: Optional[MedicalHistory] = Field(None, description="Patient medical history")
    current_inquiry: str = Field(..., description="Current health inquiry")
    session_type: str = Field(default="diagnosis", description="Type of session")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Session start time")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Session metadata")
    
    @property
    def age(self) -> Optional[int]:
        """Calculate patient age if date of birth is available."""
        if self.patient_info and self.patient_info.date_of_birth:
            today = date.today()
            dob = self.patient_info.date_of_birth
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return None