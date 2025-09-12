#!/usr/bin/env python3
from agno_test.agents.healthcare.teams.research_testing_team import ResearchTestingTeam

if __name__ == "__main__":
    team = ResearchTestingTeam()
    team.print_response("Patient reports chest pain and shortness of breath")
