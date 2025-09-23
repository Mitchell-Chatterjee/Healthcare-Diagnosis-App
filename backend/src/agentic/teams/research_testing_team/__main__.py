#!/usr/bin/env python3
from backend.src.agentic.agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse
from backend.src.agentic.teams.research_testing_team.schemas import ResearchTestingRequest
from src.agentic.teams.research_testing_team.team import ResearchTestingTeam

if __name__ == "__main__":
    differential_diagnosis = DifferentialDiagnosisResponse(
        clinical_summary="35-year-old patient presenting with chest pain, shortness of breath, and fatigue for 3 days",
        possible_conditions=[
            "Myocardial infarction",
            "Pulmonary embolism", 
            "Pneumonia",
            "Anxiety disorder",
            "Gastroesophageal reflux disease"
        ],
        most_likely_condition="Myocardial infarction",
        recommended_tests=[
            "ECG",
            "Cardiac troponins",
            "Chest X-ray",
            "D-dimer",
            "Complete blood count"
        ],
        red_flags=[
            "Severe chest pain radiating to arm or jaw",
            "Difficulty breathing at rest",
            "Syncope or near-syncope",
            "Diaphoresis with chest pain"
        ]
    )

    input = ResearchTestingRequest(
        original_inquiry="Patient reports chest pain and shortness of breath",
        differential_diagnosis=differential_diagnosis
    )
    
    team = ResearchTestingTeam()
    team.print_response(input)