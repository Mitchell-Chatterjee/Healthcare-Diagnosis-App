from agno.agent import Agent
from agno.tools.reasoning import ReasoningTools
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.final_diagnosis_agent.prompts import final_diagnosis_agent_description, final_diagnosis_agent_instructions
from src.agentic.agents.final_diagnosis_agent.schemas import FinalDiagnosisResponse

import asyncio


class FinalDiagnosisAgent(Agent):
    """
    Agent specialized in providing final diagnosis by synthesizing information from all previous workflow steps.
    
    This agent integrates:
    - Differential diagnosis candidates 
    - Research findings
    - Test results
    
    To provide a conclusive diagnosis with confidence assessment and educational disclaimers.
    
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Final Diagnosis Agent", **kwargs):
        """
        Initialize the Final Diagnosis Agent.
        
        Args:
            name: The name of the agent
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            model=LanguageModelFactory.create_default_model(),
            tools=[ReasoningTools],
            description=final_diagnosis_agent_description,
            instructions=final_diagnosis_agent_instructions,
            output_schema=FinalDiagnosisResponse,
            **kwargs
        )
