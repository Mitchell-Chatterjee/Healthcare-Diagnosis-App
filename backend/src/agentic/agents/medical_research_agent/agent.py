from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.reasoning import ReasoningTools
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.medical_research_agent.prompts import medical_research_agent_description, medical_research_agent_instructions

# TODO: Fix test utils imports when test infrastructure is ready
# from deepeval.tracing import observe, update_current_span
# from deepeval.test_case import LLMTestCase
# from src.tests.test_utils.utils.eval_metrics import answer_relevancy_metrics

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
            model=LanguageModelFactory.create_default_model(),
            tools=[
                GoogleSearchTools(),
                ReasoningTools(add_instructions=True),
            ],
            description=medical_research_agent_description,
            instructions=medical_research_agent_instructions,
            **kwargs
        )
