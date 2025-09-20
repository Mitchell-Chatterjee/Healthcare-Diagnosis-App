#!/usr/bin/env python3
from src.agentic.agents.symptom_extraction_agent.agent import SymptomExtractionAgent

if __name__ == "__main__":
    agent = SymptomExtractionAgent()
    agent.print_response("I have a headache and feel nauseous")
