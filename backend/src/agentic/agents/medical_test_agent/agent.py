from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.medical_test_agent.prompts import medical_test_agent_description, medical_test_agent_instructions
from src.agentic.tools.medical_test_tools import MedicalTestTools

from deepeval.test_case import ToolCall

import asyncio

# Optionally add memory/storage if needed
# from agno.storage.sqlite import SqliteStorage
# from agno.memory.v2.db.sqlite import SqliteMemoryDb
# from agno.memory.v2.memory import Memory


from deepeval.tracing import observe, update_current_span
from deepeval.test_case import LLMTestCase
from deepeval.metrics import ToolCorrectnessMetric

class MedicalTestAgent(Agent):
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
            show_tool_calls=True,
            **kwargs
        )
