#!/usr/bin/env python3
import asyncio
from agno_test.agents.healthcare.workflows.healthcare_workflow import HealthcareWorkflow

if __name__ == "__main__":
    workflow = HealthcareWorkflow()
    workflow.print_response("Patient reports chest pain and shortness of breath")
