from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.reasoning import ReasoningTools
from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.research.utils import health_research_agent_prompt_tools

from deepeval.tracing import observe, update_current_span
from deepeval.test_case import LLMTestCase
from agno_test.agents.healthcare.test_utils.utils.eval_metrics import answer_relevancy_metrics

import asyncio

# Optionally add memory/storage if needed
# from agno.storage.sqlite import SqliteStorage
# from agno.memory.v2.db.sqlite import SqliteMemoryDb
# from agno.memory.v2.memory import Memory

class MedicalResearchAgent(Agent):
    """
    Agent specialized in conducting medical research based on symptoms.
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Medical Research Agent", enable_memory: bool = False, **kwargs):
        """
        Initialize the Medical Research Agent.
        
        Args:
            name: The name of the agent
            enable_memory: Whether to enable memory features
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            model=mistral_small_32_online(),
            tools=[
                GoogleSearchTools(),
                ReasoningTools(add_instructions=True),
            ],
            instructions=health_research_agent_prompt_tools,
            show_tool_calls=True,
            **kwargs
        )
        
        # MEMORY MANAGEMENT (optional)
        # if enable_memory:
        #     self.storage = storage
        #     self.memory = memory
        #     self.add_history_to_messages = True
        #     self.num_history_responses = 3
        #     self.enable_user_memories = True

    @observe(type="agent", name="Research Agent", metrics=answer_relevancy_metrics(threshold=0))
    def run(self, message: str, *args, **kwargs):
        """Run the agent synchronously."""
        response = super().run(message=message, *args, **kwargs)

        # Extract content from RunResponse for evaluation
        update_current_span(test_case=LLMTestCase(input=message, actual_output=response.content))

        return response
