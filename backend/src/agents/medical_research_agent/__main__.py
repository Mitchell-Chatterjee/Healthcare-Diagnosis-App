#!/usr/bin/env python3
from agno_test.agents.healthcare.agents.medical_research_agent import MedicalResearchAgent

if __name__ == "__main__":
    agent = MedicalResearchAgent()
    response = agent.print_response("Research symptoms for headache and fever")
