import pytest
from agno_test.agents.healthcare.agents.symptom_extraction_agent import SymptomExtractionAgent


class TestSymptomExtractionAgent:
    """Test cases for the Symptom Extraction Agent."""
    
    def test_agent_initialization(self):
        """Test that the agent initializes correctly."""
        agent = SymptomExtractionAgent()
        assert agent.name == "Symptom Extraction Agent"
        assert agent.model is not None
        assert agent.tools is None  # This agent doesn't use tools
    
    def test_agent_with_custom_name(self):
        """Test agent initialization with custom name."""
        custom_name = "Custom Symptom Agent"
        agent = SymptomExtractionAgent(name=custom_name)
        assert agent.name == custom_name
