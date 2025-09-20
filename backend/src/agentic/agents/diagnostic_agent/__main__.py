#!/usr/bin/env python3
from agno_test.agents.healthcare.agents.diagnostic_agent import DiagnosticAgent

if __name__ == "__main__":
    agent = DiagnosticAgent()
    response = agent.print_response("Test diagnostic query")