from agno.workflow.v2.step import Step
from agno_test.agents.healthcare.agents.symptom_extraction_agent import SymptomExtractionAgent
from agno_test.agents.healthcare.agents.diagnostic_agent import DiagnosticAgent
from agno_test.agents.healthcare.teams.research_testing_team import ResearchTestingTeam

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
        agent=DiagnosticAgent(name="Diagnostic Agent"),
    )

def get_workflow_steps():
    """Get all workflow steps in order."""
    return [
        create_symptom_extraction_step(),
        create_research_testing_step(),
        create_diagnostic_step()
    ]
