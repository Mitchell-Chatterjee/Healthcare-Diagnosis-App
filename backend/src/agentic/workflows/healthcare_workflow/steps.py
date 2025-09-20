from agno.workflow import Step
from src.agentic.agents.symptom_extraction_agent.agent import SymptomExtractionAgent
from src.agentic.agents.differential_diagnosis_agent.agent import DifferentialDiagnosisAgent
from src.agentic.teams.research_testing_team.team import ResearchTestingTeam

def create_symptom_extraction_step():
    """Create the symptom extraction step."""
    return Step(
        name="Symptom Extraction Step",
        agent=SymptomExtractionAgent(name="Symptom Extraction Agent"),
    )

def create_research_testing_step():
    """Create the research and testing step."""
    return Step(
        name="Research and Testing Step", 
        team=ResearchTestingTeam(),
    )

def create_diagnostic_step():
    """Create the diagnostic step."""
    return Step(
        name="Diagnostic Step",
        agent=DifferentialDiagnosisAgent(name="Differential Diagnosis Agent"),
    )

def get_workflow_steps():
    """Get all workflow steps in order."""
    return [
        create_symptom_extraction_step(),
        create_research_testing_step(),
        create_diagnostic_step()
    ]
