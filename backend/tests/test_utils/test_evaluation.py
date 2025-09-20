import pytest
import asyncio
import random
from functools import partial
from deepeval import assert_test
from deepeval.dataset import Golden
from deepeval.tracing import observe, update_current_span
from agno_test.agents.healthcare.test_utils.plausible_health_scenarios import all_test_scenarios, HealthcareScenario
from agno_test.agents.healthcare.healthcare_workflow import HealthcareWorkflow

healthcare_workflow = HealthcareWorkflow(use_storage=False)
# healthcare_workflow.workflow_session_state["eval_llm"] = model

# Set to True to run only the first test, False to run all tests
RUN_SINGLE_TEST = True
test_scenarios = [all_test_scenarios[random.randint(0, len(all_test_scenarios) - 1)]] if RUN_SINGLE_TEST else all_test_scenarios


@pytest.mark.parametrize("scenario", test_scenarios)
def test_healthcare_workflow(scenario: HealthcareScenario):
    """Test healthcare workflow with component-level evaluations."""
    # Create an observed callback with the scenario already bound
    golden = Golden(input=scenario.user_query, name='Test 1')
    # Bind the expected tools to the workflow session state
    healthcare_workflow.workflow_session_state["expected_tools_by_agent"] = scenario.expected_tools_by_agent
    healthcare_workflow.workflow_session_state["expected_output"] = scenario.diagnosis
    # Use assert_test with observed_callback for component-level evaluation
    assert_test(golden=golden, observed_callback=healthcare_workflow.run)