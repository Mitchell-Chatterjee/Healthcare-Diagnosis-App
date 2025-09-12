import functools
from typing import List, Union, Optional
from agno_test.agents.healthcare.test_utils.instrumentation.base.decorator_base import ConditionalInstrumentation
from deepeval.tracing import observe, update_current_span
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import BaseMetric
from agno.team.team import Team
from agno.workflow.workflow import Workflow
from agno.agent.agent import Agent
from agno.run.response import RunResponse
from agno.run.team import TeamRunResponse
from agno.run.v2.workflow import WorkflowRunResponse

AgnoInstance = Union[Agent, Team, Workflow]
AgnoResponse = Union[RunResponse, WorkflowRunResponse, TeamRunResponse]


def create_test_case(instance: AgnoInstance, message: str, response: AgnoResponse) -> LLMTestCase:
    """Create an LLMTestCase for the current interaction."""
    actual_output = response.content
    
    tools_called = None
    expected_tools = None
    if hasattr(response, "tools") and response.tools:
        tools_called = [ToolCall(name=tool.tool_name) for tool in response.tools]
        expected_tools = instance.workflow_session_state.get("expected_tools_by_agent", {}).get(instance.__class__.__name__, None)

    return LLMTestCase(
        input=message,
        actual_output=actual_output,
        expected_output=instance.workflow_session_state.get("expected_output", None),
        retrieval_context=[actual_output], 
        tools_called=tools_called, 
        expected_tools=expected_tools
    )


def observe_run_method(
    instance_type: str,
    metrics: List[BaseMetric],
    name: Optional[str] = None
):
    """
    Function decorator that instruments run methods with observability.
    REQUIRES explicit metrics selection - no defaults allowed.
    
    Usage:
        class MyAgent(Agent):
            @observe_run_method("agent", [AnswerRelevancyMetric(threshold=0.8)])
            def run(self, message, *args, **kwargs) -> RunResponse:
                return super().run(message, *args, **kwargs)
    """
    # Require explicit metrics - no defaults allowed
    if not metrics:
        raise ValueError(f"Explicit metrics required. Specify metrics=[YourMetric()]")
    
    def decorator(run_method):
        @functools.wraps(run_method)
        @observe(type=instance_type, name=name, metrics=metrics)
        def instrumented_run(self, message, *args, **kwargs) -> AgnoResponse:
            """Instrumented run method with observability and type safety."""        
            response: AgnoResponse = run_method(self, message, *args, **kwargs)
            update_current_span(test_case=create_test_case(self, message, response))
            return response
            
        return instrumented_run
    
    return decorator


# Convenience decorators for specific types with explicit metrics required
@ConditionalInstrumentation.wrap
def observe_agent_run(metrics: List[BaseMetric], name: Optional[str] = None):
    """
    Method decorator specifically for Agent run methods - REQUIRES explicit metrics.
    
    Args:
        metrics: REQUIRED list of metrics - developer must explicitly choose
        name: Custom name for tracing
    
    Usage:
        class MyAgent(Agent):
            @observe_agent_run([AnswerRelevancyMetric(threshold=0.8)])
            def run(self, message, *args, **kwargs) -> RunResponse:
                return super().run(message, *args, **kwargs)
    """
    return observe_run_method("agent", metrics, name)


@ConditionalInstrumentation.wrap
def observe_team_run(metrics: List[BaseMetric], name: Optional[str] = None):
    """
    Method decorator specifically for Team run methods - REQUIRES explicit metrics.
    
    Args:
        metrics: REQUIRED list of metrics - developer must explicitly choose
        name: Custom name for tracing
    
    Usage:
        class MyTeam(Team):
            @observe_team_run([ContextualRelevancyMetric(threshold=0.7)])
            def run(self, message, *args, **kwargs) -> TeamRunResponse:
                return super().run(message, *args, **kwargs)
    """ 
    return observe_run_method("team", metrics, name)


@ConditionalInstrumentation.wrap
def observe_workflow_run(metrics: List[BaseMetric], name: Optional[str] = None):
    """
    Method decorator specifically for Workflow run methods - REQUIRES explicit metrics.
    
    Args:
        metrics: REQUIRED list of metrics - developer must explicitly choose  
        name: Custom name for tracing
    
    Usage:
        class MyWorkflow(Workflow):
            @observe_workflow_run([CorrectnessMetric(), AnswerRelevancyMetric(threshold=0.8)])
            def run(self, message, *args, **kwargs) -> WorkflowRunResponse:
                return super().run(message, *args, **kwargs)
    """
    return observe_run_method("workflow", metrics, name)