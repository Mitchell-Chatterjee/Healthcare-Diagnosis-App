#!/usr/bin/env python3
from agno_test.agents.healthcare.agents.medical_test_agent import MedicalTestAgent

if __name__ == "__main__":
    agent = MedicalTestAgent()
    agent.print_response("Run CBC and metabolic panel tests")
