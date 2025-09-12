from agno.agent import Agent
from agno.run.response import RunResponse
from agno.tools.reasoning import ReasoningTools
from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.medical_test.utils import health_agent_prompt_tools
from agno_test.agents.healthcare.tools.medical_test_tools import MedicalTestTools

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
            model=mistral_small_32_online(),
            tools=[
                MedicalTestTools(),
                ReasoningTools(add_instructions=True),
            ],
            instructions=health_agent_prompt_tools,
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
    
    async def run_test(self, patient_inquiry: str, symptoms: list[str], research_summary: str) -> dict:
        """
        Run medical tests based on patient inquiry, symptoms, and research summary.
        
        Args:
            patient_inquiry: The patient's original inquiry
            symptoms: List of extracted symptoms
            research_summary: Research findings and recommendations
            
        Returns:
            dict: Dictionary containing test results and analysis
        """
        # Construct query with all three inputs
        query = f"""
        PATIENT INQUIRY: {patient_inquiry}
        
        EXTRACTED SYMPTOMS: {', '.join(symptoms)}
        
        RESEARCH SUMMARY: {research_summary}
        
        Based on this information, please select and execute the most appropriate diagnostic tests from your available tools.
        """
        
        response = await self.aprint_response(
            message=query, 
            show_full_reasoning=True, 
            reasoning=True
        )
        
        return {
            "patient_inquiry": patient_inquiry,
            "symptoms": symptoms,
            "research_summary": research_summary,
            "test_results": response
        }

    @observe(type="agent", name="Medical Test Agent", 
             metrics=[ToolCorrectnessMetric(threshold=0.0)])
    def run(self, message, *args, **kwargs):
        """Run the agent synchronously."""
        response = super().run(message=message, *args, **kwargs)

        # Capture the tools called by the agent
        tools = [ToolCall(name=tool.tool_name) for tool in response.tools]

        # Retrieve the expected tools for this agent from the workflow session state
        expected_tools = self.workflow_session_state.get("expected_tools_by_agent", {})\
            .get(MedicalTestAgent.__name__, [])

        # Ensure tools and expected_tools are not empty
        if not tools or not expected_tools:
            print("Warning: Tools or expected tools are missing.")
            return response

        # Update the current span with the LLMTestCase
        update_current_span(test_case=LLMTestCase(
            input=message, 
            actual_output=response.content, 
            tools_called=tools, 
            expected_tools=expected_tools)
        )
        return response