import pytest
from agno_test.agents.healthcare.agents.medical_research_agent import MedicalResearchAgent


class TestMedicalResearchAgent:
    """Test cases for the Medical Research Agent."""
    
    def test_agent_initialization(self):
        """Test that the agent initializes correctly."""
        agent = MedicalResearchAgent()
        assert agent.name == "Medical Research Agent"
        assert agent.model is not None
        assert len(agent.tools) > 0
    
    def test_agent_with_custom_name(self):
        """Test agent initialization with custom name."""
        custom_name = "Custom Research Agent"
        agent = MedicalResearchAgent(name=custom_name)
        assert agent.name == custom_name
    
    def test_agent_with_memory_disabled(self):
        """Test agent initialization with memory disabled."""
        agent = MedicalResearchAgent(enable_memory=False)
        assert agent.name == "Medical Research Agent"
