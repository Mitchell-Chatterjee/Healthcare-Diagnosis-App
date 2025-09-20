"""
Base configuration classes for the Healthcare Diagnosis App.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from pathlib import Path
import os


class BaseConfig(BaseModel):
    """Base configuration class with common settings."""
    
    # Environment
    environment: str = Field(default="development", description="Environment name")
    debug: bool = Field(default=False, description="Debug mode")
    
    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log format string"
    )
    
    # Timeouts
    default_timeout: int = Field(default=30, description="Default timeout in seconds")
    max_retries: int = Field(default=3, description="Maximum retry attempts")
    
    class Config:
        env_prefix = "HEALTHCARE_"
        case_sensitive = False


class ModelConfig(BaseConfig):
    """Configuration for AI models."""
    
    # Model settings
    model_provider: str = Field(default="openai", description="AI model provider")
    model_name: str = Field(default="gpt-4", description="Model name")
    api_key: Optional[str] = Field(None, description="API key for model provider")
    api_base_url: Optional[str] = Field(None, description="Base URL for API")
    
    # Model parameters
    max_tokens: int = Field(default=2000, description="Maximum tokens per response")
    temperature: float = Field(default=0.1, description="Model temperature")
    top_p: float = Field(default=1.0, description="Top-p sampling")
    frequency_penalty: float = Field(default=0.0, description="Frequency penalty")
    presence_penalty: float = Field(default=0.0, description="Presence penalty")
    
    # Rate limiting
    rate_limit_per_minute: int = Field(default=60, description="API calls per minute")
    concurrent_requests: int = Field(default=5, description="Max concurrent requests")


class DatabaseConfig(BaseConfig):
    """Database configuration."""
    
    # Connection settings
    database_url: Optional[str] = Field(None, description="Database connection URL")
    pool_size: int = Field(default=10, description="Connection pool size")
    max_overflow: int = Field(default=20, description="Max pool overflow")
    connection_timeout: int = Field(default=30, description="Connection timeout")
    query_timeout: int = Field(default=60, description="Query timeout")
    
    # Migration settings
    auto_upgrade: bool = Field(default=False, description="Auto-run migrations")
    migration_timeout: int = Field(default=300, description="Migration timeout")


class CacheConfig(BaseConfig):
    """Cache configuration."""
    
    # Redis settings
    redis_url: Optional[str] = Field(None, description="Redis connection URL")
    redis_password: Optional[str] = Field(None, description="Redis password")
    redis_db: int = Field(default=0, description="Redis database number")
    
    # Cache settings
    default_ttl: int = Field(default=3600, description="Default TTL in seconds")
    agent_response_ttl: int = Field(default=1800, description="Agent response TTL")
    workflow_state_ttl: int = Field(default=86400, description="Workflow state TTL")
    
    # Memory cache fallback
    enable_memory_cache: bool = Field(default=True, description="Enable in-memory cache")
    max_memory_cache_size: int = Field(default=1000, description="Max items in memory cache")


class SecurityConfig(BaseConfig):
    """Security configuration."""
    
    # Authentication
    secret_key: Optional[str] = Field(None, description="Application secret key")
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(default=30, description="Access token expiry")
    refresh_token_expire_days: int = Field(default=7, description="Refresh token expiry")
    
    # Rate limiting  
    rate_limit_enabled: bool = Field(default=True, description="Enable rate limiting")
    rate_limit_per_minute: int = Field(default=60, description="Requests per minute")
    rate_limit_burst: int = Field(default=10, description="Burst allowance")
    
    # CORS
    cors_origins: List[str] = Field(default=["*"], description="CORS allowed origins")
    cors_methods: List[str] = Field(default=["GET", "POST"], description="CORS allowed methods")
    
    # Security headers
    enable_security_headers: bool = Field(default=True, description="Enable security headers")


class MedicalConfig(BaseConfig):
    """Medical-specific configuration."""
    
    # Diagnosis settings
    confidence_threshold: float = Field(default=0.7, description="Minimum confidence for diagnosis")
    max_differential_diagnoses: int = Field(default=5, description="Max differential diagnoses")
    max_symptoms_per_inquiry: int = Field(default=20, description="Max symptoms to extract")
    
    # Safety settings
    enable_medical_disclaimers: bool = Field(default=True, description="Show medical disclaimers")
    emergency_keyword_detection: bool = Field(default=True, description="Detect emergency keywords")
    require_professional_review: bool = Field(default=True, description="Require professional review")
    
    # Test settings
    max_tests_per_session: int = Field(default=10, description="Max tests per diagnostic session")
    test_timeout: int = Field(default=120, description="Test execution timeout")
    
    # Workflow settings
    max_workflow_iterations: int = Field(default=3, description="Max workflow iterations")
    workflow_step_timeout: int = Field(default=120, description="Workflow step timeout")


class APIConfig(BaseConfig):
    """API configuration."""
    
    # Server settings
    host: str = Field(default="0.0.0.0", description="Host address")
    port: int = Field(default=8000, description="Port number")
    workers: int = Field(default=1, description="Number of worker processes")
    
    # Request settings
    max_request_size: int = Field(default=10 * 1024 * 1024, description="Max request size in bytes")
    request_timeout: int = Field(default=300, description="Request timeout")
    
    # API versioning
    api_version: str = Field(default="v1", description="API version")
    api_prefix: str = Field(default="/api", description="API prefix")
    
    # Documentation
    enable_docs: bool = Field(default=True, description="Enable API documentation")
    docs_url: str = Field(default="/docs", description="Documentation URL")
    openapi_url: str = Field(default="/openapi.json", description="OpenAPI schema URL")


class HealthcareConfig(BaseConfig):
    """Main healthcare application configuration."""
    
    # Sub-configurations
    model: ModelConfig = Field(default_factory=ModelConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    cache: CacheConfig = Field(default_factory=CacheConfig)
    security: SecurityConfig = Field(default_factory=SecurityConfig)
    medical: MedicalConfig = Field(default_factory=MedicalConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    
    # Application metadata
    app_name: str = Field(default="Healthcare Diagnosis App", description="Application name")
    app_version: str = Field(default="1.0.0", description="Application version")
    app_description: str = Field(
        default="AI-powered healthcare diagnosis assistance",
        description="Application description"
    )
    
    @classmethod
    def from_env(cls) -> "HealthcareConfig":
        """Create configuration from environment variables."""
        return cls()
    
    @classmethod  
    def from_file(cls, config_path: Path) -> "HealthcareConfig":
        """Create configuration from file."""
        # This would load from YAML/JSON file
        # Implementation depends on chosen format
        return cls()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return self.dict()
    
    def validate_config(self) -> List[str]:
        """Validate configuration and return any errors."""
        errors = []
        
        # Validate required settings
        if not self.model.api_key and self.model.model_provider != "test":
            errors.append("API key required for model provider")
            
        if self.security.secret_key is None:
            errors.append("Secret key required for security")
            
        # Validate numeric ranges
        if self.medical.confidence_threshold < 0 or self.medical.confidence_threshold > 1:
            errors.append("Confidence threshold must be between 0 and 1")
            
        return errors