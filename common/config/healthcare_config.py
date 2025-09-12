class HealthcareConfig:
    """Base configuration for healthcare components."""
    
    # Database file paths
    DB_DIR = "tmp"
    
    # Standard database files
    RESEARCH_TESTING_DB = f"{DB_DIR}/research_testing_team.db"
    WORKFLOW_DB = f"{DB_DIR}/workflow_storage.db"
    HEALTHCARE_TEAM_DB = f"{DB_DIR}/healthcare_team_agent.db"
    
    # Component settings
    SHOW_TOOL_CALLS = True
    SHOW_MEMBER_RESPONSES = True
    ADD_HISTORY_TO_MESSAGES = True
    ENABLE_USER_MEMORIES = True
    
    # Evaluation settings
    DEFAULT_CORRECTNESS_THRESHOLD = 0
    DEFAULT_RELEVANCY_THRESHOLD = 0.5


class AgentConfig(HealthcareConfig):
    """Configuration specific to agents."""
    
    DEFAULT_SHOW_TOOL_CALLS = True


class TeamConfig(HealthcareConfig):
    """Configuration specific to teams."""
    
    DEFAULT_MODE = "coordinate"
    DEFAULT_SHOW_MEMBER_RESPONSES = True


class WorkflowConfig(HealthcareConfig):
    """Configuration specific to workflows."""
    
    DEFAULT_USE_STORAGE = True
    DEFAULT_STREAM = True
    DEFAULT_STREAM_INTERMEDIATE_STEPS = True
