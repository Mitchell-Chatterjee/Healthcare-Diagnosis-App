import os
import sys
import pytest
from pathlib import Path

# Ensure backend root is on sys.path so 'tests.*' and 'src.*' imports resolve
# regardless of which directory deepeval test run is invoked from
_backend_root = Path(__file__).parent.parent.parent
if str(_backend_root) not in sys.path:
    sys.path.insert(0, str(_backend_root))

from deepeval.models import AzureOpenAIModel

from tests.test_utils.utils.eval_model_config import EvalModelConfig

def pytest_configure(config):
    """Set up the model before test collection."""
    # Enable component-eval gated metrics during tests
    os.environ["DEEPEVAL_COMPONENT_EVAL"] = "1"

    # Note: For public use, set these values via environment variables
    # AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, etc.
    azure_model = AzureOpenAIModel(
        model_name="Azure OpenAI 4o",
        deployment_name="gpt-4o-2",
        azure_openai_api_key=os.getenv("AZURE_OPENAI_API_KEY", "your-api-key-here"),
        openai_api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://your-endpoint.openai.azure.com")
    )
    EvalModelConfig.set_model(azure_model)
