# Backend Tests - Healthcare Diagnosis App

This directory contains test utilities and shared testing infrastructure for the healthcare diagnosis backend.

## 📁 Structure

```
tests/
├── README.md                  # This file
├── conftest.py               # Pytest configuration and fixtures
├── test_utils/              # Original test utilities (moved from root)
└── integration/             # Integration test suites
    ├── test_full_workflow.py
    ├── test_agent_interactions.py
    └── test_api_endpoints.py
```

## 🧪 Test Categories

### Unit Tests
Individual component tests are located within each package:
- `src/agents/*/tests/` - Agent-specific tests
- `src/teams/*/tests/` - Team-specific tests  
- `src/agentic/workflows/*/tests/` - Workflow-specific tests

### Integration Tests
Cross-component integration tests are in this directory:
- Full workflow end-to-end tests
- Agent-to-team interaction tests
- API endpoint integration tests

### Test Utilities
Shared testing infrastructure and utilities:
- Mock medical data generators
- Test scenario builders
- Evaluation metrics and validation
- Performance benchmarking tools

## 🚀 Running Tests

```bash
# Run all tests
pytest

# Run specific test category
pytest tests/integration/

# Run with coverage
pytest --cov=src

# Run performance tests
pytest tests/performance/
```

## 📊 Test Data

The `test_utils/` directory contains:
- `plausible_health_scenarios.py` - Realistic medical scenarios
- `evaluation_utils.py` - Testing and validation utilities
- `instrumentation/` - Testing instrumentation and metrics