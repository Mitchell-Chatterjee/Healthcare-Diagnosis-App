from agno_test.utils.models import mistral_small_32_online


def get_default_model():
    """Get the default model for healthcare agents."""
    return mistral_small_32_online()


class HealthcareModelConfig:
    """Configuration class for healthcare models."""
    
    @staticmethod
    def get_agent_model():
        """Get the standard model for agents."""
        return mistral_small_32_online()
    
    @staticmethod
    def get_team_model():
        """Get the standard model for teams."""
        return mistral_small_32_online()
    
    @staticmethod
    def get_workflow_model():
        """Get the standard model for workflows."""
        return mistral_small_32_online()
    
    @staticmethod
    def get_memory_model():
        """Get the model for memory operations.""" 
        return mistral_small_32_online()
