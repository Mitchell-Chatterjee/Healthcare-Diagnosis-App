"""
Utility functions for evaluation-related checks.
"""

import os

def component_eval_enabled() -> bool:
    """Check if instrumentation is enabled via the environment variable."""
    return os.getenv("DEEPEVAL_COMPONENT_EVAL") == "1"
