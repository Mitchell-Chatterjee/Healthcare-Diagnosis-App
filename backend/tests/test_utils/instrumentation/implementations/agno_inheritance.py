import functools
from typing import List, Union
from deepeval.tracing import observe, update_current_span
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import BaseMetric
from agno.team.team import Team
from agno.workflow.workflow import Workflow
from agno.agent.agent import Agent
from agno.run.workflow import WorkflowRunOutput
from agno.run.agent import RunOutput
from agno.run.team import TeamRunOutput

from tests.test_utils.instrumentation.base.inheritance_base import InstrumentedBase

AgnoInstance = Union[Agent, Team, Workflow]
AgnoResponse = Union[RunOutput, WorkflowRunOutput, TeamRunOutput]


def create_test_case(instance: AgnoInstance, message: str, response: AgnoResponse) -> LLMTestCase:
    """Create an LLMTestCase for the current interaction."""
    from pydantic import BaseModel as PydanticBaseModel
    raw_output = response.content
    if isinstance(raw_output, PydanticBaseModel):
        actual_output = raw_output.model_dump_json()
    else:
        actual_output = str(raw_output) if raw_output is not None else ""
    session_state = instance.session_state or {}

    tools_called = None
    expected_tools = None
    if hasattr(response, "tools") and response.tools:
        tools_called = [ToolCall(name=tool.tool_name) for tool in response.tools]
        expected_tools = session_state.get("expected_tools_by_agent", {}).get(instance.__class__.__name__, None)  # TODO: Make this expected into a shared enum

    return LLMTestCase(
        input=message,
        actual_output=actual_output,
        expected_output=session_state.get("expected_output", None), # TODO: Also this one
        retrieval_context=[actual_output], 
        tools_called=tools_called, 
        expected_tools=expected_tools
    )


def create_instrumented_run_method(
    original_run_method,
    instance_type: str,
    instance_name: str,
    observability_metrics: List[BaseMetric]
):
    """Create an instrumented version of the run method with observability metrics.
    
    Args:
        original_run_method: The original run method to instrument
        instance_type: Type of instance ("agent", "team", "workflow")
        instance_name: Name for observability tracing
        observability_metrics: List of metrics to apply
        
    Returns:
        Instrumented run method that returns AgnoResponse
    """
    @functools.wraps(original_run_method)
    @observe(type=instance_type, name=instance_name, metrics=observability_metrics)
    def instrumented_run(self, input, *args, **kwargs) -> AgnoResponse:
        """Instrumented run method with observability and type safety."""        
        response: AgnoResponse = original_run_method(self, input, *args, **kwargs)
        update_current_span(test_case=create_test_case(self, input, response))
        return response
        
    return instrumented_run


def create_instrumented_workflow_run_method(
    original_run_method,
    instance_type: str,
    instance_name: str,
    observability_metrics: List[BaseMetric]
):
    """Create an instrumented version of the run method for Workflows.
    
    Workflows use 'input' as the parameter name instead of 'message'.
    """
    @functools.wraps(original_run_method)
    @observe(type=instance_type, name=instance_name, metrics=observability_metrics)
    def instrumented_run(self, input, *args, **kwargs) -> AgnoResponse:
        """Instrumented run method for workflows."""
        response: AgnoResponse = original_run_method(self, input, *args, **kwargs)
        update_current_span(test_case=create_test_case(self, input, response))
        return response

    return instrumented_run

# Direct Inheritance Base Classes with Required Explicit Metrics

class InstrumentedAgent(Agent, InstrumentedBase):
    """Instrumented Agent base class with automatic run method instrumentation.
    
    Requires explicit observability_metrics implementation.
    
    Usage:
        class MyAgent(InstrumentedAgent):
            @classmethod
            def observability_metrics(cls) -> List[BaseMetric]:
                return [AnswerRelevancyMetric(threshold=0.8)]
    """
    _instance_type = 'agent'
    
    @classmethod
    def _instrument_run_method(cls):
        """Instrument the run method for this agent class."""        
        original_run = cls.run
        cls.run = create_instrumented_run_method(
            original_run, cls._instance_type, cls.__name__, cls.observability_metrics()
        )


class InstrumentedTeam(Team, InstrumentedBase):
    """Instrumented Team base class with automatic run method instrumentation.
    
    Requires explicit observability_metrics implementation.
    
    Usage:
        class MyTeam(InstrumentedTeam):
            @classmethod
            def observability_metrics(cls) -> List[BaseMetric]:
                return [ContextualRelevancyMetric(threshold=0.7)]
    """
    _instance_type = 'team'
    
    @classmethod
    def _instrument_run_method(cls):
        """Instrument the run method for this team class."""
        original_run = cls.run
        cls.run = create_instrumented_run_method(
            original_run, cls._instance_type, cls.__name__, cls.observability_metrics()
        )


class InstrumentedWorkflow(Workflow, InstrumentedBase):
    """Instrumented Workflow base class with automatic run method instrumentation.
    
    Requires explicit observability_metrics implementation.
    
    Usage:
        class MyWorkflow(InstrumentedWorkflow):
            @classmethod
            def observability_metrics(cls) -> List[BaseMetric]:
                return [CorrectnessMetric(), AnswerRelevancyMetric(threshold=0.8)]
    """
    _instance_type = 'workflow'
    
    @classmethod
    def _instrument_run_method(cls):
        """Instrument the run method for this workflow class."""
        original_run = cls.run
        cls.run = create_instrumented_workflow_run_method(
            original_run, cls._instance_type, cls.__name__, cls.observability_metrics()
        )