"""Comprehensive configuration system for the Healthcare Diagnosis App.

This module provides secure configuration management with environment variable
loading, validation, and support for multiple AI model providers.
"""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class AzureOpenAIConfig(BaseModel):
    """Configuration for Azure OpenAI service."""
    api_key: str
    endpoint: str
    deployment_name: str
    api_version: str
    model_name: str

class LanguageModelsConfig(BaseModel):
    """Configuration for language models."""
    azure_gpt_oss: AzureOpenAIConfig

class AppConfig(BaseSettings):
    """Main application configuration that loads all settings."""
    language_models: LanguageModelsConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__"
    )

# Module-level singleton - most Pythonic approach
_config: Optional[AppConfig] = None

def get_config() -> AppConfig:
    """Get the global configuration instance (module-level singleton)."""
    global _config
    if _config is None:
        _config = AppConfig()
    return _config

def reload_config() -> AppConfig:
    """Reload the configuration (useful for testing or config changes)."""
    global _config
    _config = None
    return get_config()
