from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.symptom_extraction.utils import symptom_extraction_agent_prompt_tools

import asyncio


class SymptomExtractionAgent(Agent):
    """
    Agent specialized in extracting symptoms from patient inquiries.
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Symptom Extraction Agent", **kwargs):
        """
        Initialize the Symptom Extraction Agent.
        
        Args:
            name: The name of the agent
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            model=mistral_small_32_online(),
            tools=None,
            instructions=symptom_extraction_agent_prompt_tools,
            show_tool_calls=True,
            **kwargs
        )
