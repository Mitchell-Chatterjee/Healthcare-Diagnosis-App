import asyncio
from agno.team.team import Team
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.medical_research_agent.agent import MedicalResearchAgent
from src.agentic.agents.medical_test_agent.agent import MedicalTestAgent
# TODO: Fix test utils imports when test infrastructure is ready
# from src.tests.test_utils.utils.eval_metrics import contextual_relevancy_metrics
# from src.tests.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedTeam

from src.agentic.teams.research_testing_team.roles import define_team_roles
from src.agentic.teams.research_testing_team.coordination import get_team_instructions


class ResearchTestingTeam(Team):
    """
    A team that coordinates research and testing agents to handle complex medical inquiries.
    """

    def __init__(self, **kwargs):
        """
        Initialize the Research Testing Team.
        
        Args:
            **kwargs: Additional arguments passed to the base Team class
        """
        
        # Get team configuration
        roles = define_team_roles()
        
        super().__init__(
            name="Research Testing Team",
            description="A team that coordinates research and testing agents to handle complex medical inquiries.",
            mode=roles["coordination_mode"],
            team_id="research_testing_team",
            model=LanguageModelFactory.create_default_model(),
            members=[
                MedicalResearchAgent(name="Medical Research Agent"),
                MedicalTestAgent(name="Healthcare Test Agent")
            ],
            instructions=get_team_instructions(),
            show_tool_calls=True,
            show_members_responses=True,
            storage=storage,
            add_history_to_messages=True,
            enable_user_memories=True,
            memory=memory,
            **kwargs
        )
    
    @classmethod
    def observability_metrics(cls):
        # TODO: Implement metrics when test infrastructure is ready
        return []
