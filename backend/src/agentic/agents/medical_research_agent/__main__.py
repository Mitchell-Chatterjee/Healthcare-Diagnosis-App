#!/usr/bin/env python3
from src.agentic.agents.medical_research_agent.agent import MedicalResearchAgent

if __name__ == "__main__":
    agent = MedicalResearchAgent()
    response = agent.print_response("Research symptoms for headache and fever")
