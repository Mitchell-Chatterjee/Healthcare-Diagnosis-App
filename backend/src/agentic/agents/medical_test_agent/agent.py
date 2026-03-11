from agno.tools.reasoning import ReasoningTools
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.medical_test_agent.prompts import medical_test_agent_description, medical_test_agent_instructions
from src.agentic.agents.medical_test_agent.tools.medical_test_tools import MedicalTestTools
from tests.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedAgent
from tests.test_utils.utils.eval_metrics import tool_correctness_metrics


class MedicalTestAgent(InstrumentedAgent):
    """
    Agent specialized in selecting and executing medical diagnostic tests.
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Medical Test Agent", enable_memory: bool = False, **kwargs):
        """
        Initialize the Medical Test Agent.
        
        Args:
            name: The name of the agent
            enable_memory: Whether to enable memory features
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            model=LanguageModelFactory.create_default_model(),
            tools=[
                MedicalTestTools(),
                ReasoningTools(add_instructions=True),
            ],
            description=medical_test_agent_description,
            instructions=medical_test_agent_instructions,
            **kwargs
        )

    @classmethod
    def observability_metrics(cls):
        return tool_correctness_metrics()
