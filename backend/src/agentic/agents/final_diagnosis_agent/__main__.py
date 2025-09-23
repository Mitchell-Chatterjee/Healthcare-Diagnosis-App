#!/usr/bin/env python3
from src.agentic.agents.final_diagnosis_agent.agent import FinalDiagnosisAgent
from src.agentic.agents.final_diagnosis_agent.schemas import FinalDiagnosisRequest
from src.agentic.agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse
from src.agentic.teams.research_testing_team.schemas import (
    ResearchTestingResponse, 
    ResearchFinding, 
    TestResult
)

if __name__ == "__main__":    
    # Create realistic differential diagnosis results
    differential_diagnosis = DifferentialDiagnosisResponse(
        clinical_summary="35-year-old patient with acute chest pain, shortness of breath, and diaphoresis for 3 hours",
        possible_conditions=[
            "Myocardial infarction",
            "Pulmonary embolism",
            "Pneumonia", 
            "Panic attack"
        ],
        most_likely_condition="Myocardial infarction",
        recommended_tests=[
            "ECG",
            "Cardiac troponins",
            "Chest X-ray",
            "D-dimer"
        ],
        red_flags=[
            "Chest pain radiating to left arm",
            "Severe shortness of breath",
            "Diaphoresis"
        ]
    )
    
    # Create realistic research and testing results
    research_testing = ResearchTestingResponse(
        original_inquiry="I have severe chest pain and can't breathe properly",
        differential_context=differential_diagnosis,
        research_findings=[
            ResearchFinding(
                topic="Acute Myocardial Infarction",
                summary="STEMI presents with severe chest pain, ST elevation on ECG, elevated troponins",
                sources=["ACC/AHA Guidelines", "ESC Guidelines"],
                relevance="High - matches patient presentation"
            )
        ],
        test_results=[
            TestResult(
                test_name="ECG",
                result="ST elevation in leads II, III, aVF indicating inferior STEMI",
                normal_range="Normal ST segments",
                interpretation="Abnormal - consistent with acute MI"
            ),
            TestResult(
                test_name="Troponin I",
                result="15.2 ng/mL",
                normal_range="<0.04 ng/mL", 
                interpretation="Severely elevated - confirms myocardial injury"
            )
        ],
        additional_observations=[
            "Patient appears diaphoretic and anxious",
            "Blood pressure 90/60 mmHg - hypotensive"
        ],
        completion_status="Complete"
    )
    
    # Create the final diagnosis request with all workflow data
    sample_request = FinalDiagnosisRequest(
        original_inquiry="I have severe chest pain and can't breathe properly",
        differential_diagnosis=differential_diagnosis,
        research_testing=research_testing
    )
    
    agent = FinalDiagnosisAgent()
    agent.print_response(sample_request)
