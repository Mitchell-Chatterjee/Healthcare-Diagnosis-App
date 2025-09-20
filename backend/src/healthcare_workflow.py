import asyncio
import random
from textwrap import dedent
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.test_utils.plausible_health_scenarios import all_test_scenarios
from agno_test.agents.healthcare.agents.symptom_extraction.symptom_extraction_agent import SymptomExtractionAgent
from agno_test.agents.healthcare.agents.diagnostic.diagnostic_agent import DiagnosticAgent
from agno_test.agents.healthcare.healthcare_team import ResearchTestingTeam
from agno_test.agents.healthcare.test_utils.utils.eval_metrics import answer_relevancy_metrics, correctness_metrics, combine_metrics
from agno_test.agents.healthcare.test_utils.instrumentation.implementations.agno_decorator import observe_workflow_run

# Database file for memory and storage
workflow_db_file = "tmp/workflow_storage.db"
# Session storage saves a Team's sessions in a database and enables Teams to have multi-turn conversations.
workflow_storage = SqliteStorage(table_name="workflow_storage", db_file=workflow_db_file)
workflow_memory = Memory(
    # Use any model for creating memories
    model=mistral_small_32_online(),
    db=SqliteMemoryDb(table_name="workflow_memories", db_file=workflow_db_file),
)

# Initialize agents as global variables for use in steps
symptom_agent = SymptomExtractionAgent(name="Symptom Extraction Agent")
research_testing_team = ResearchTestingTeam()
diagnostic_agent = DiagnosticAgent(name="Diagnostic Agent")

# Define steps using the correct Step pattern
symptom_extraction_step = Step(
    name="Symptom Extraction Step",
    agent=symptom_agent,
)

research_testing_step = Step(
    name="Research and Testing Step", 
    team=research_testing_team,
)

diagnostic_step = Step(
    name="Diagnostic Step",
    agent=diagnostic_agent,
)


class HealthcareWorkflow(Workflow):
    """A workflow that orchestrates healthcare agents for symptom extraction, 
    research, testing, and diagnosis."""

    description: str = "A workflow that orchestrates healthcare agents for " \
    "symptom extraction, research, testing, and diagnosis."

    def __init__(self, use_storage: bool = True):
        """Initialize the healthcare workflow with all specialized agents."""
        # Use Step objects for proper sequential execution with optional storage
        super().__init__(
            name="Healthcare Workflow",
            description=self.description,
            storage=workflow_storage if use_storage else None,
            steps=[symptom_extraction_step, research_testing_step, diagnostic_step],
            workflow_session_state={},  # Initialize empty workflow session state
        )

    @observe_workflow_run(
            metrics=combine_metrics([correctness_metrics(threshold=0), 
            answer_relevancy_metrics(threshold=0.5)]), name="Healthcare Workflow")
    def run(self, message, *args, **kwargs):
        """Run the workflow asynchronously."""
        return super().run(message=message, *args, **kwargs)

#### DEBUGGING ####


async def test_healthcare_workflow():
    """Test the Healthcare Workflow with various medical scenarios"""
    print("=== Creating Healthcare Workflow ===")

    # Create the workflow
    generate_diagnosis = HealthcareWorkflow()
    
    # Select one test scenario at random from all available scenarios
    selected_scenario = random.choice(all_test_scenarios)
    test_case = selected_scenario.user_query
    
    print(f"Running 1 randomly selected test scenario from {len(all_test_scenarios)} available scenarios")
    print(f"Expected diagnosis: {selected_scenario.diagnosis}")
    print(f"Recommended tests: {', '.join(selected_scenario.expected_tools_by_agent)}")

    print(f"\n{'=' * 60}")
    print(f"Test Case: {test_case}")
    print("=" * 60)

    try:
        # Use aprint_response with streaming for proper step-by-step execution
        await generate_diagnosis.aprint_response(
            message=test_case,
            markdown=True,
            stream=True,
            stream_intermediate_steps=True,
        )
    except Exception as e:
        print(f"Error in test case: {e}")

    print(f"\nCompleted test case")


if __name__ == "__main__":
    # Test the full healthcare team
    asyncio.run(test_healthcare_workflow())