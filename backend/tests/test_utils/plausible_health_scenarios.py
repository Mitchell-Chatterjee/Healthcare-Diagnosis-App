# Plausible healthcare scenarios for patient interactions
# Each scenario includes a user query, expected tools by agent, and a diagnosis
# Tools are organized by agent type and aligned with available tools in the system

from dataclasses import dataclass
from typing import List, Dict
from deepeval.test_case import ToolCall

from backend.src.agentic.agents.medical_test_agent.agent import MedicalTestAgent



@dataclass
class HealthcareScenario:
    """A healthcare scenario containing a patient query, expected tools by agent, and diagnosis."""
    user_query: str
    expected_tools_by_agent: Dict[str, List[str]]  # Agent-specific expected tools
    diagnosis: str


# Complete list of healthcare test scenarios - duplicates removed, best versions kept
all_test_scenarios = [
    HealthcareScenario(
        user_query="I have a fever, chills, and a persistent cough.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='cbc'), ToolCall(name='chest_xray'), ToolCall(name='blood_cultures')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Pneumonia"
    ),
    HealthcareScenario(
        user_query="I feel tired all the time and have pale skin. I also get dizzy when I stand up.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='cbc'), ToolCall(name='ferritin'), ToolCall(name='vitamin_d_level'), ToolCall(name='bmp')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Iron Deficiency Anemia with Orthostatic Hypotension"
    ),
    HealthcareScenario(
        user_query="I have excessive thirst, frequent urination, and blurred vision.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='bmp'), ToolCall(name='hemoglobin_a1c'), ToolCall(name='urinalysis')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Diabetes Mellitus Type 2"
    ),
    HealthcareScenario(
        user_query="I have chest pain and shortness of breath, especially when walking.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='ecg'), ToolCall(name='troponin'), ToolCall(name='chest_xray'), ToolCall(name='echocardiogram')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Exertional Angina"
    ),
    HealthcareScenario(
        user_query="I have joint pain and stiffness, especially in the morning in my hands and feet.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='rheumatoid_factor'), ToolCall(name='ana_test'), ToolCall(name='crp'), ToolCall(name='esr')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Rheumatoid Arthritis"
    ),
    HealthcareScenario(
        user_query="I have a lump in my breast.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='mammogram'), ToolCall(name='ultrasound'), ToolCall(name='cbc')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Breast Cancer"
    ),
    HealthcareScenario(
        user_query="I have abdominal pain and blood in my stool for the past week.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='colonoscopy'), ToolCall(name='stool_culture'), ToolCall(name='cbc'), ToolCall(name='cmp')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Inflammatory Bowel Disease"
    ),
    HealthcareScenario(
        user_query="I have a sore throat and swollen lymph nodes.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='rapid_strep_test'), ToolCall(name='cbc')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Strep Throat"
    ),
    HealthcareScenario(
        user_query="I have severe headaches and blurred vision.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='mri_scan'), ToolCall(name='blood_gas_analysis'), ToolCall(name='cbc')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Hypertension with Possible Stroke"
    ),
    HealthcareScenario(
        user_query="I have unexplained weight loss and night sweats.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='chest_xray'), ToolCall(name='blood_cultures'), ToolCall(name='ct_scan')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Tuberculosis"
    ),
    HealthcareScenario(
        user_query="I have difficulty breathing and a tight feeling in my chest.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='pulmonary_function_tests'), ToolCall(name='chest_xray'), ToolCall(name='ecg')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Asthma"
    ),
    HealthcareScenario(
        user_query="I have yellowing of my skin and eyes, and dark urine.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='liver_function_tests'), ToolCall(name='hepatitis_panel'), ToolCall(name='cbc')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Hepatitis"
    ),
    HealthcareScenario(
        user_query="I have been feeling very cold, gaining weight, and my hair is thinning.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='thyroid_function_tests'), ToolCall(name='cbc'), ToolCall(name='lipid_panel')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Hypothyroidism"
    ),
    HealthcareScenario(
        user_query="I have sharp chest pain that gets worse when I breathe deeply.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='chest_xray'), ToolCall(name='d_dimer'), ToolCall(name='ecg')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Pulmonary Embolism"
    ),
    HealthcareScenario(
        user_query="I have been having memory problems and confusion lately.",
        expected_tools_by_agent={
            f'{MedicalTestAgent.__name__}': [ToolCall(name='mri_scan'), ToolCall(name='thyroid_function_tests'), ToolCall(name='vitamin_d_level')],
            'research_agent': [ToolCall(name='google_search')],
            'diagnostic_agent': []
        },
        diagnosis="Cognitive Impairment"
    )
]
