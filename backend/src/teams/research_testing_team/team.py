import asyncio
from agno.team.team import Team
from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.medical_research_agent import MedicalResearchAgent
from agno_test.agents.healthcare.agents.medical_test_agent import MedicalTestAgent
from agno_test.agents.healthcare.test_utils.utils.eval_metrics import contextual_relevancy_metrics
from agno_test.agents.healthcare.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedTeam

from .roles import define_team_roles
from .coordination import get_team_instructions, setup_team_storage_and_memory


class ResearchTestingTeam(InstrumentedTeam):
    """
    A team that coordinates research and testing agents to handle complex medical inquiries.
    """

    def __init__(self, **kwargs):
        """
        Initialize the Research Testing Team.
        
        Args:
            **kwargs: Additional arguments passed to the base Team class
        """
        # Setup storage and memory
        storage, memory = setup_team_storage_and_memory()
        
        # Get team configuration
        roles = define_team_roles()
        
        super().__init__(
            name="Research Testing Team",
            description="A team that coordinates research and testing agents to handle complex medical inquiries.",
            mode=roles["coordination_mode"],
            team_id="research_testing_team",
            model=mistral_small_32_online(),
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
        return contextual_relevancy_metrics()
