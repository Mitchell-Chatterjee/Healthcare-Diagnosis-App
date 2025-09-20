import pytest
from agno_test.agents.healthcare.agents.diagnostic_agent import DiagnosticAgent


class TestDiagnosticAgent:
    """Test cases for the Diagnostic Agent."""
    
    def test_agent_initialization(self):
        """Test that the agent initializes correctly."""
        agent = DiagnosticAgent()
        assert agent.name == "Diagnostic Agent"
        assert agent.model is not None
        assert len(agent.tools) > 0
    
    def test_agent_with_custom_name(self):
        """Test agent initialization with custom name."""
        custom_name = "Custom Diagnostic Agent"
        agent = DiagnosticAgent(name=custom_name)
        assert agent.name == custom_name
