# Healthcare Diagnosis App - Backend

The backend for the Healthcare Diagnosis App, built with Python and the Agno framework for AI agent orchestration.

## 🏗️ Architecture

The backend follows a clean, modular architecture with three main directories:

```
backend/
├── src/                    # All source code
│   ├── agents/            # Individual AI agents
│   ├── teams/             # Multi-agent teams  
│   ├── workflows/         # Orchestration workflows
│   ├── api/               # REST API endpoints
│   ├── services/          # Business logic services
│   ├── common/            # Shared utilities & config
│   └── tools/             # Custom tools & integrations
├── utils/                 # Development utilities & demos
└── tests/                 # Test infrastructure & shared fixtures
```

## 🤖 Core Components

### Agents (`src/agents/`)
Specialized AI agents for specific healthcare tasks:
- **DiagnosticAgent**: Provides diagnostic analysis based on symptoms and test results
- **MedicalResearchAgent**: Conducts medical research using search capabilities  
- **MedicalTestAgent**: Coordinates and executes medical diagnostic tests
- **SymptomExtractionAgent**: Extracts and structures symptoms from patient inquiries

### Teams (`src/teams/`)
Multi-agent collaboration systems:
- **ResearchTestingTeam**: Coordinates research and testing agents for comprehensive medical analysis

### Workflows (`src/workflows/`)  
End-to-end process orchestration:
- **HealthcareWorkflow**: Complete diagnostic workflow from symptom intake to final diagnosis

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip or uv package manager

### Installation
```bash
cd backend
pip install -r requirements.txt
# or
uv install
```

### Basic Usage
```python
from backend.src import DiagnosticAgent, ResearchTestingTeam, HealthcareWorkflow

# Use individual agents
agent = DiagnosticAgent()
result = agent.run("Patient has chest pain and shortness of breath")

# Use coordinated teams  
team = ResearchTestingTeam()
analysis = team.run("Investigate chest pain symptoms")

# Use full workflow
workflow = HealthcareWorkflow()
diagnosis = workflow.run("Patient inquiry about chest pain")
```

### Running Demos
```bash
# Simple workflow demonstration
python -m utils.simple_healthcare_workflow_demo

# Individual agent testing
python -m src.agents.diagnostic_agent
python -m src.agents.medical_research_agent
```

## 🔧 Development

### Project Structure Standards
All packages follow consistent structure patterns:

#### Agent Package Structure
```
agents/agent_name/
├── __init__.py         # Package exports
├── __main__.py         # Standalone entry point  
├── agent.py            # Main agent implementation
├── prompts.py          # Agent instructions & descriptions
├── schemas.py          # Pydantic data models
└── tests/              # Unit tests
    ├── __init__.py
    ├── test_agent.py
    └── test_schemas.py
```

#### Team Package Structure  
```
teams/team_name/
├── __init__.py         # Package exports
├── __main__.py         # Standalone entry point
├── team.py             # Team orchestration logic
├── roles.py            # Agent role definitions
├── coordination.py     # Collaboration patterns
├── schemas.py          # Team data models  
└── tests/              # Unit tests
```

#### Workflow Package Structure
```
workflows/workflow_name/
├── __init__.py         # Package exports
├── __main__.py         # Standalone entry point
├── workflow.py         # Main workflow implementation
├── steps.py            # Individual workflow steps
├── config.py           # Workflow configuration
├── schemas.py          # Workflow data models
└── tests/              # Unit tests
```

### Testing
```bash
# Run all tests
pytest

# Run specific component tests
pytest src/agents/diagnostic_agent/tests/
pytest src/teams/research_testing_team/tests/
pytest src/workflows/healthcare_workflow/tests/

# Run with coverage
pytest --cov=src

# Run integration tests
pytest tests/integration/
```

### Code Quality
```bash
# Format code
black src/ utils/ tests/

# Lint code  
flake8 src/ utils/ tests/

# Type checking
mypy src/
```

## 📊 API Integration

### REST API (`src/api/`)
FastAPI-based REST endpoints for external integration:
- Health check endpoints
- Diagnosis workflow API
- Agent-specific endpoints
- Real-time status monitoring

### Services Layer (`src/services/`)
Business logic services that coordinate agents and workflows:
- Diagnosis orchestration service
- Patient data management service  
- Results processing service
- Integration services

## 🛠️ Configuration

### Environment Variables
```bash
# Model configuration
HEALTHCARE_MODEL_PROVIDER=openai
HEALTHCARE_API_KEY=your-api-key
HEALTHCARE_MODEL_NAME=gpt-4

# Database (if used)
HEALTHCARE_DB_URL=postgresql://...

# Logging
LOG_LEVEL=INFO
```

### Configuration Files
- `src/common/config/healthcare_config.py` - Main configuration
- `src/workflows/healthcare_workflow/config.py` - Workflow settings
- `tests/conftest.py` - Test configuration

## 🔍 Monitoring & Observability

The backend includes comprehensive monitoring:
- Agent execution tracking
- Workflow performance metrics
- Error monitoring and alerting
- Medical decision audit trails

## 🏥 Medical Safety

This system includes safety measures:
- Medical disclaimer requirements
- Confidence scoring for all diagnoses
- Audit trails for medical decisions
- Integration with existing healthcare systems

## 📚 Documentation

- [Agent Development Guide](docs/agent-development.md)
- [Team Coordination Patterns](docs/team-patterns.md)  
- [Workflow Design Guidelines](docs/workflow-design.md)
- [API Documentation](docs/api-reference.md)

## 🤝 Contributing

1. Follow the established package structure patterns
2. Add comprehensive tests for new components
3. Update documentation for public interfaces
4. Ensure medical safety considerations are addressed
5. Include proper error handling and logging

## ⚖️ License & Compliance

This project includes medical AI functionality and should be used in accordance with:
- Healthcare regulations (HIPAA, GDPR, etc.)
- Medical device standards where applicable  
- AI ethics guidelines
- Professional medical oversight requirements

See [LICENSE](../LICENSE) and [SECURITY.md](../SECURITY.md) for details.