import pytest
from agno_test.agents.healthcare.agents.medical_test_agent import MedicalTestAgent


class TestMedicalTestAgent:
    """Test cases for the Medical Test Agent."""
    
    def test_agent_initialization(self):
        """Test that the agent initializes correctly."""
        agent = MedicalTestAgent()
        assert agent.name == "Medical Test Agent"
        assert agent.model is not None
        assert len(agent.tools) > 0
    
    def test_agent_with_custom_name(self):
        """Test agent initialization with custom name."""
        custom_name = "Custom Test Agent"
        agent = MedicalTestAgent(name=custom_name)
        assert agent.name == custom_name
    
    def test_agent_with_memory_disabled(self):
        """Test agent initialization with memory disabled."""
        agent = MedicalTestAgent(enable_memory=False)
        assert agent.name == "Medical Test Agent"
