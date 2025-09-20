import asyncio
import random
from agno.workflow import Workflow

from .steps import get_workflow_steps


class HealthcareWorkflow(Workflow):
    """A workflow that orchestrates healthcare agents for symptom extraction, 
    research, testing, and diagnosis."""

    def __init__(self, use_storage: bool = True):
        """Initialize the healthcare workflow with all specialized agents."""
        
        # Use Step objects for proper sequential execution with optional storage
        super().__init__(
            name="HealthcareWorkflow",
            description="A workflow for healthcare-related tasks",
            storage=use_storage,
            steps=get_workflow_steps(),
            workflow_session_state={},  # Initialize empty workflow session state
        )