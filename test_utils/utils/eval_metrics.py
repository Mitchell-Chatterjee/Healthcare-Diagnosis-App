from typing import List
from functools import partial

from agno_test.agents.healthcare.test_utils.utils.evaluation_utils import component_eval_enabled
from deepeval.metrics import AnswerRelevancyMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCaseParams
from deepeval.metrics import GEval, BaseMetric
from deepeval.metrics.g_eval import Rubric
from agno_test.agents.healthcare.test_utils.utils.eval_model_config import EvalModelConfig


Correctness_metric = partial(
        GEval,
        name="Correctness",
        criteria="Determine whether the 'actual output' is factually correct and aligns with the 'expected output', allowing for flexibility in wording while ensuring core meaning is preserved.",
        evaluation_steps=[
            "Check whether the facts in 'actual output' contradict any facts in 'expected output'",
            "Verify that key information from 'expected output' is present in 'actual output'",
            "Allow flexibility in wording, phrasing, and minor details unless explicitly critical",
            "Penalize omission of important details but not additional non-contradictory information",
            "Focus on core meaning alignment rather than exact word matching"
        ],
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        rubric=[
            Rubric(score_range=(0, 2), expected_outcome="Factually incorrect or contradicts 'expected output'."),
            Rubric(score_range=(3, 5), expected_outcome="Partially correct but missing key information or has minor contradictions."),
            Rubric(score_range=(6, 8), expected_outcome="Mostly correct with all main points covered but may lack some details."),
            Rubric(score_range=(9, 10), expected_outcome="Fully correct with all essential information accurately represented.")
        ]
    )


def answer_relevancy_metrics(threshold: float = 0.0) -> List[AnswerRelevancyMetric]:
    """Return AnswerRelevancyMetric list only when eval is enabled; else empty list.

    Prevents importing/initializing LLM clients outside test runs.
    """
    if component_eval_enabled():
        model = EvalModelConfig.get_model()
        return [AnswerRelevancyMetric(model=model, threshold=threshold)]
    return []


def contextual_relevancy_metrics(threshold: float = 0.0) -> List[ContextualRelevancyMetric]:
    """Return ContextualRelevancyMetric list only when eval is enabled; else empty list."""
    if component_eval_enabled():
        model = EvalModelConfig.get_model()
        return [ContextualRelevancyMetric(model=model, threshold=threshold)]
    return []

def correctness_metrics(threshold: float = 0.0) -> List[GEval]:
    """Return GEval list only when eval is enabled; else empty list."""
    if component_eval_enabled():
        model = EvalModelConfig.get_model()
        return [Correctness_metric(model=model, threshold=threshold)]
    return []  

def combine_metrics(metrics: List[List[BaseMetric]]) -> List[BaseMetric]:
    """Combine multiple lists of metrics into a single list."""
    combined = []
    for metric_list in metrics:
        combined.extend(metric_list)
    return combined
