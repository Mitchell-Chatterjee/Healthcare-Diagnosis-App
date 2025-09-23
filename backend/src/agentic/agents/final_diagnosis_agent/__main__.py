#!/usr/bin/env python3
from src.agentic.agents.final_diagnosis_agent.agent import FinalDiagnosisAgent
from src.agentic.agents.final_diagnosis_agent.schemas import FinalDiagnosisRequest

if __name__ == "__main__":
    agent = FinalDiagnosisAgent()
    
    # Example usage with sample input
    sample_request = FinalDiagnosisRequest(
        patient_inquiry="I have a headache and feel nauseous",
        clinical_summary="Patient reports headache and nausea",
        differential_candidates=[
            {"condition": "Migraine", "probability": "moderate"},
            {"condition": "Tension headache", "probability": "high"}
        ]
    )
    
    agent.print_response(sample_request)
