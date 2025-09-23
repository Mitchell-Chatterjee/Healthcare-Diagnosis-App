from agno.workflow import Workflow, Step

from backend.src.agentic.agents.differential_diagnosis_agent.agent import DifferentialDiagnosisAgent
from backend.src.agentic.agents.final_diagnosis_agent.agent import FinalDiagnosisAgent
from backend.src.agentic.teams.research_testing_team.team import ResearchTestingTeam


class HealthcareWorkflow(Workflow):
    """A workflow that orchestrates healthcare agents for comprehensive medical analysis.
    
    Workflow Steps:
    1. Differential Diagnosis - Extract symptoms and generate candidate diagnoses using clinical methodology
    2. Research and Testing - Gather evidence and recommend/perform tests
    3. Final Diagnosis - Synthesize all information into conclusive diagnosis with educational disclaimers
    
    All outputs include educational disclaimers emphasizing this is for learning purposes only.
    """

    def __init__(self, use_storage: bool = True):
        """Initialize the healthcare workflow with all specialized agents in proper sequence."""
        self.session_state = {}
        
        # Use Step objects for proper sequential execution with optional storage
        super().__init__(
            name="Healthcare Workflow",
            description="A comprehensive workflow for educational medical analysis",
            storage=use_storage,
            steps=[
                Step(name="Differential Diagnosis Step", agent=DifferentialDiagnosisAgent()),
                Step(name="Research and Testing Step", team=ResearchTestingTeam()),
                Step(name="Final Diagnosis Step", agent=FinalDiagnosisAgent()),
            ]
        )