#!/usr/bin/env python3
from agno_test.agents.healthcare.agents.symptom_extraction_agent import SymptomExtractionAgent

if __name__ == "__main__":
    agent = SymptomExtractionAgent()
    agent.print_response("I have a headache and feel nauseous")
