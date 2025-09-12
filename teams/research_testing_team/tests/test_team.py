import pytest
from agno_test.agents.healthcare.teams.research_testing_team import ResearchTestingTeam


class TestResearchTestingTeam:
    """Test cases for the Research Testing Team."""
    
    def test_team_initialization(self):
        """Test that the team initializes correctly."""
        team = ResearchTestingTeam()
        assert team.name == "Research Testing Team"
        assert team.model is not None
        assert len(team.members) == 2
        assert team.team_id == "research_testing_team"
    
    def test_team_has_correct_members(self):
        """Test that the team has the correct member agents."""
        team = ResearchTestingTeam()
        member_names = [member.name for member in team.members]
        assert "Medical Research Agent" in member_names
        assert "Healthcare Test Agent" in member_names
    
    def test_team_observability_metrics(self):
        """Test that observability metrics are available."""
        metrics = ResearchTestingTeam.observability_metrics()
        assert metrics is not None
