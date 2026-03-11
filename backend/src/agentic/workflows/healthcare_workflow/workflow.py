from agno.workflow import Workflow, Step

from src.agentic.agents.differential_diagnosis_agent.agent import DifferentialDiagnosisAgent
from src.agentic.agents.final_diagnosis_agent.agent import FinalDiagnosisAgent
from src.agentic.teams.research_testing_team.team import ResearchTestingTeam
from tests.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedWorkflow
from tests.test_utils.utils.eval_metrics import answer_relevancy_metrics


class HealthcareWorkflow(InstrumentedWorkflow):
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
            steps=[
                Step(name="Differential Diagnosis Step", agent=DifferentialDiagnosisAgent()),
                Step(name="Research and Testing Step", team=ResearchTestingTeam()),
                Step(name="Final Diagnosis Step", agent=FinalDiagnosisAgent()),
            ],
            stream_intermediate_steps=True,
            stream=False,
        )

    @classmethod
    def observability_metrics(cls):
        return answer_relevancy_metrics()