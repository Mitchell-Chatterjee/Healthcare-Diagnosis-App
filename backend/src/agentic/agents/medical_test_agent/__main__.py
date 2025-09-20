#!/usr/bin/env python3
from src.agentic.agents.medical_test_agent.agent import MedicalTestAgent

if __name__ == "__main__":
    agent = MedicalTestAgent()
    agent.print_response("Run CBC and metabolic panel tests")
