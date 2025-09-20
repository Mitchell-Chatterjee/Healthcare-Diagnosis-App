"""
Base decorator class for DeepEval.
"""
from agno_test.agents.healthcare.test_utils.utils.evaluation_utils import component_eval_enabled

class ConditionalInstrumentation:
    """Utility for wrapping decorators with conditional logic."""

    @staticmethod
    def wrap(decorator_factory):
        """Wrap a decorator factory with conditional logic."""
        def conditional_decorator(*args, **kwargs):
            if not component_eval_enabled():
                # Return a no-op decorator
                def noop_decorator(run_method):
                    return run_method
                return noop_decorator
            # Return the actual decorator
            return decorator_factory(*args, **kwargs)
        return conditional_decorator
