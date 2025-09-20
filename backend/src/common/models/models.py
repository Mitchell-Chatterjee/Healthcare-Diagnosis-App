"""Model configurations for healthcare diagnosis app."""

from agno.models.azure import AzureOpenAI
from agno.models.base import Model
from ..config.config import get_config

class LanguageModelFactory:
    """Factory for creating language models with abstracted interface for agno."""
    
    @staticmethod
    def create_gpt_oss() -> Model:
        """Create a GPT-OSS model using centralized configuration."""
        config = get_config()
        azure_config = config.language_models.azure_gpt_oss
        return AzureOpenAI(
            id=azure_config.model_name,
            api_key=azure_config.api_key,
            azure_deployment=azure_config.deployment_name,
            azure_endpoint=azure_config.endpoint,
            api_version=azure_config.api_version
        )
    
    # Public methods - direct and discoverable
    @staticmethod
    def create_default_model() -> Model:
        """Create the default language model (Azure OpenAI)."""
        return LanguageModelFactory.create_gpt_oss()
