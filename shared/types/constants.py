"""
System constants and configuration values for the Healthcare Diagnosis App.
"""

# Medical Constants
MAX_SYMPTOMS_PER_INQUIRY = 20
MAX_DIFFERENTIAL_DIAGNOSES = 5
DEFAULT_CONFIDENCE_THRESHOLD = 0.7
MAX_SESSION_DURATION_HOURS = 24

# API Constants
DEFAULT_TIMEOUT_SECONDS = 30
MAX_RETRIES = 3
DEFAULT_RATE_LIMIT_PER_MINUTE = 60

# Agent Configuration
AGENT_MAX_REASONING_STEPS = 10
AGENT_RESPONSE_MAX_TOKENS = 2000
TEAM_COORDINATION_TIMEOUT = 300  # 5 minutes

# Workflow Configuration
WORKFLOW_STEP_TIMEOUT = 120  # 2 minutes per step
MAX_WORKFLOW_ITERATIONS = 3
WORKFLOW_SESSION_TTL = 86400  # 24 hours

# Medical Terminology
URGENCY_KEYWORDS = [
    "emergency", "urgent", "severe pain", "chest pain", 
    "difficulty breathing", "bleeding", "unconscious", "severe"
]

CHRONIC_KEYWORDS = [
    "chronic", "ongoing", "persistent", "long-term", 
    "for months", "for years", "always have"
]

# Test Categories
BASIC_TESTS = [
    "Complete Blood Count (CBC)",
    "Basic Metabolic Panel (BMP)", 
    "Urinalysis",
    "Chest X-ray"
]

CARDIAC_TESTS = [
    "Electrocardiogram (ECG)",
    "Troponin I",
    "Troponin T", 
    "Echocardiogram",
    "Stress Test"
]

DIAGNOSTIC_TESTS = [
    "CT Scan",
    "MRI",
    "Ultrasound",
    "Blood Culture",
    "Biopsy"
]

# Error Messages
ERROR_MESSAGES = {
    "INVALID_INPUT": "Invalid input provided",
    "TIMEOUT": "Operation timed out",
    "AGENT_ERROR": "Agent processing error",
    "WORKFLOW_ERROR": "Workflow execution error",
    "MEDICAL_DISCLAIMER": "This is not medical advice. Consult a healthcare provider.",
    "INSUFFICIENT_DATA": "Insufficient data for reliable diagnosis",
    "EMERGENCY_WARNING": "Seek immediate medical attention for emergency symptoms"
}

# Medical Disclaimers
MEDICAL_DISCLAIMER = """
IMPORTANT MEDICAL DISCLAIMER:
This system provides information for educational purposes only and is not intended 
as a substitute for professional medical advice, diagnosis, or treatment. Always 
seek the advice of your physician or other qualified health provider with any 
questions you may have regarding a medical condition. Never disregard professional 
medical advice or delay in seeking it because of something you have read here.
In case of a medical emergency, call your local emergency services immediately.
"""

EMERGENCY_DISCLAIMER = """
EMERGENCY WARNING:
If you are experiencing a medical emergency, stop using this system and 
call your local emergency services (911 in the US) immediately.
"""

# File Size Limits
MAX_UPLOAD_SIZE_MB = 10
SUPPORTED_IMAGE_TYPES = ["jpg", "jpeg", "png", "gif"]
SUPPORTED_DOCUMENT_TYPES = ["pdf", "txt", "doc", "docx"]

# Logging Configuration
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Database Configuration
DEFAULT_DATABASE_POOL_SIZE = 10
DATABASE_CONNECTION_TIMEOUT = 30
QUERY_TIMEOUT = 60

# Cache Configuration  
DEFAULT_CACHE_TTL = 3600  # 1 hour
AGENT_RESPONSE_CACHE_TTL = 1800  # 30 minutes
WORKFLOW_STATE_CACHE_TTL = 86400  # 24 hours