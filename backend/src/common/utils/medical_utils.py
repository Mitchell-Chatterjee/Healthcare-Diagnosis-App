def format_medical_response(sections: dict) -> str:
    """Format a medical response with standardized sections."""
    formatted = ""
    
    for section_name, content in sections.items():
        formatted += f"**{section_name}:**\n"
        if isinstance(content, list):
            formatted += "\n".join(f"- {item}" for item in content)
        else:
            formatted += str(content)
        formatted += "\n\n"
    
    return formatted.strip()


def extract_symptoms_from_text(text: str) -> list:
    """Extract symptoms from text using basic pattern matching."""
    # This is a simplified implementation - in practice you'd use more sophisticated NLP
    common_symptom_patterns = [
        "pain", "ache", "hurt", "sore", "burning", "stinging",
        "nausea", "nauseous", "dizzy", "headache", "fever",
        "cough", "shortness of breath", "difficulty breathing",
        "fatigue", "tired", "weakness", "swelling"
    ]
    
    text_lower = text.lower()
    found_symptoms = []
    
    for pattern in common_symptom_patterns:
        if pattern in text_lower:
            found_symptoms.append(pattern)
    
    return found_symptoms


def validate_medical_input(text: str) -> bool:
    """Validate that input text contains medical-related content."""
    if not text or len(text.strip()) < 5:
        return False
    
    medical_keywords = [
        "pain", "symptom", "feel", "hurt", "sick", "doctor",
        "medical", "health", "diagnosis", "test", "treatment"
    ]
    
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in medical_keywords)
