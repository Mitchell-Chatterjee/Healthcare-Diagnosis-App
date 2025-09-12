from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.diagnostic.utils import diagnostic_agent_prompt_tools

import asyncio


class DiagnosticAgent(Agent):
    """
    Agent specialized in providing diagnostic analysis based on symptoms and test results.
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Diagnostic Agent", **kwargs):
        """
        Initialize the Diagnostic Agent.
        
        Args:
            name: The name of the agent
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            model=mistral_small_32_online(),
            tools=[
                ReasoningTools(add_instructions=True),
            ],
            instructions=diagnostic_agent_prompt_tools,
            show_tool_calls=True,
            **kwargs
        )