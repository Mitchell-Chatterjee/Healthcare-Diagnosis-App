import asyncio
import random
from agno.workflow.v2.workflow import Workflow
from agno_test.agents.healthcare.test_utils.plausible_health_scenarios import all_test_scenarios
from agno_test.agents.healthcare.test_utils.utils.eval_metrics import answer_relevancy_metrics, correctness_metrics, combine_metrics
from agno_test.agents.healthcare.test_utils.instrumentation.implementations.agno_decorator import observe_workflow_run

from .steps import get_workflow_steps
from .config import WorkflowConfig


class HealthcareWorkflow(Workflow):
    """A workflow that orchestrates healthcare agents for symptom extraction, 
    research, testing, and diagnosis."""

    def __init__(self, use_storage: bool = True):
        """Initialize the healthcare workflow with all specialized agents."""
        config = WorkflowConfig(use_storage)
        
        # Use Step objects for proper sequential execution with optional storage
        super().__init__(
            name=config.name,
            description=config.description,
            storage=config.storage,
            steps=get_workflow_steps(),
            workflow_session_state={},  # Initialize empty workflow session state
        )

    @observe_workflow_run(
            metrics=combine_metrics([correctness_metrics(threshold=0), 
            answer_relevancy_metrics(threshold=0.5)]), name="Healthcare Workflow")
    def run(self, message, *args, **kwargs):
        """Run the workflow asynchronously."""
        return super().run(message=message, *args, **kwargs)
