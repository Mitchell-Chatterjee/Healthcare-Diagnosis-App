import asyncio
from agno.team.team import Team
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.medical_research_agent.agent import MedicalResearchAgent
from src.agentic.agents.medical_test_agent.agent import MedicalTestAgent

from src.agentic.teams.research_testing_team.prompts import (
    research_testing_team_description,
    research_testing_team_instructions
)
from src.agentic.teams.research_testing_team.schemas import (
    ResearchTestingRequest,
    ResearchTestingResponse
)
from src.agentic.agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse


class ResearchTestingTeam(Team):
    """
    A team that coordinates research and testing agents for medical information gathering.
    """

    def __init__(self, **kwargs):
        """
        Initialize the Research Testing Team.
        
        Args:
            **kwargs: Additional arguments passed to the base Team class
        """
        
        super().__init__(
            name="Research Testing Team",
            description=research_testing_team_description,
            instructions=research_testing_team_instructions,
            model=LanguageModelFactory.create_default_model(),
            members=[
                MedicalResearchAgent(
                    name="Medical Research Agent",
                    role="Conducts comprehensive medical research and literature review"
                ),
                MedicalTestAgent(
                    name="Healthcare Test Agent", 
                    role="Orders and executes diagnostic tests based on clinical recommendations"
                )
            ],
            input_schema=ResearchTestingRequest,
            output_schema=ResearchTestingResponse,
            show_members_responses=True,
            markdown=True,
            **kwargs
        )
    
    @classmethod
    def observability_metrics(cls):
        return []
