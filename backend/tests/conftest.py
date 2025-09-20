"""
Pytest configuration and shared fixtures for Healthcare Diagnosis App tests.
"""
import pytest
import asyncio
from pathlib import Path
import sys

# Add the src directory to the Python path for imports
backend_root = Path(__file__).parent.parent
src_path = backend_root / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def sample_patient_inquiry():
    """Sample patient inquiry for testing."""
    return "I've been having chest pain and shortness of breath for the past few days"


@pytest.fixture 
def sample_symptoms():
    """Sample extracted symptoms for testing."""
    return ["chest pain", "shortness of breath", "fatigue"]


@pytest.fixture
def sample_research_summary():
    """Sample research summary for testing."""
    return """
    Based on the symptoms of chest pain and shortness of breath, possible conditions include:
    - Myocardial infarction
    - Angina pectoris  
    - Pulmonary embolism
    - Anxiety disorder
    
    Recommended tests: ECG, Troponin I, Chest X-ray, D-dimer
    """


@pytest.fixture
def sample_test_results():
    """Sample test results for testing."""
    return """
    ECG: Normal sinus rhythm, no acute changes
    Troponin I: 0.15 ng/mL (elevated, normal < 0.04)
    Chest X-ray: Clear lung fields, normal heart size
    """


@pytest.fixture
def mock_healthcare_config():
    """Mock healthcare configuration for testing."""
    return {
        "model_provider": "test",
        "api_key": "test-key",
        "max_retries": 3,
        "timeout": 30
    }


# Test markers
pytest_plugins = []

def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
    config.addinivalue_line(
        "markers", "e2e: marks tests as end-to-end tests"
    )