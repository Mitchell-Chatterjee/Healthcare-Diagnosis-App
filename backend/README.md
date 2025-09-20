# Healthcare Diagnosis App - Backend

The backend for the Healthcare Diagnosis App, built with Python and the Agno framework for AI agent orchestration.

## 🏗️ Architecture

The backend follows a clean, modular architecture with separation between AI/agentic components and traditional backend services:

```
backend/
├── src/                    # All source code
│   ├── agentic/           # All AI/LLM-powered components
│   │   ├── agents/        # Individual AI agents
│   │   ├── teams/         # Multi-agent teams  
│   │   ├── workflows/     # AI-powered workflows
│   │   └── tools/         # Agent-specific tools
│   ├── api/               # REST API endpoints
│   ├── services/          # Business logic services
│   └── common/            # Shared utilities & config
├── utils/                 # Development utilities & demos
└── tests/                 # Test infrastructure & shared fixtures
```

### � Agentic AI Architecture

The `agentic/` directory contains all AI/LLM-powered components, providing clear separation between traditional backend services and intelligent AI functionality:

- **Clear Separation of Concerns**: AI components are grouped separately from traditional web services
- **Scalable AI Architecture**: Easy to extend with new agents, teams, and workflows
- **Maintainable Codebase**: AI-specific logic is contained and organized
- **Deployment Flexibility**: Agentic components could be deployed separately if needed

## 🤖 Agentic Components

### Agents (`src/agentic/agents/`)
Specialized AI agents for specific healthcare tasks:
- **DiagnosticAgent**: Provides diagnostic analysis based on symptoms and test results
- **MedicalResearchAgent**: Conducts medical research using search capabilities  
- **MedicalTestAgent**: Coordinates and executes medical diagnostic tests
- **SymptomExtractionAgent**: Extracts and structures symptoms from patient inquiries

### Teams (`src/agentic/teams/`)
Multi-agent collaboration systems:
- **ResearchTestingTeam**: Coordinates research and testing agents for comprehensive medical analysis

### Workflows (`src/agentic/workflows/`)  
End-to-end AI-powered process orchestration:
- **HealthcareWorkflow**: Complete diagnostic workflow from symptom intake to final diagnosis

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Setup Virtual Environment

This project uses `uv` for fast Python package management. Follow these steps to set up and activate your environment:

#### 1. Install uv (if not already installed)
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

#### 2. Create and activate virtual environment
```bash
# Navigate to the backend directory
cd backend

# Create virtual environment (if it doesn't exist)
uv venv

# Activate the virtual environment
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

#### 3. Install dependencies
```bash
# Install all project dependencies
uv install

# Or install in development mode with all extras
uv install --dev
```

#### 4. Verify installation
```bash
# Check that the environment is active (you should see (.venv) in your prompt)
which python

# Verify installed packages
uv pip list
```

### Alternative: Using pip
If you prefer using pip instead of uv:
```bash
cd backend
python -m venv .venv

# Activate
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

## 🏃‍♂️ Running the Application

### Using uv run (Recommended)
`uv run` automatically manages the virtual environment for you:

```bash
# Run individual agents
uv run -m src.agentic.agents.diagnostic_agent
uv run -m src.agentic.agents.symptom_extraction_agent
uv run -m src.agentic.agents.medical_research_agent
uv run -m src.agentic.agents.medical_test_agent

# Run multi-agent teams
uv run -m src.agentic.teams.research_testing_team

# Run complete workflows
uv run -m src.agentic.workflows.healthcare_workflow

# Run demos and utilities
uv run -m utils.simple_healthcare_workflow_demo
```

### Using activated virtual environment
If you prefer to activate the environment manually:

```bash
# Activate environment
source .venv/bin/activate

# Run modules
python -m src.agentic.agents.diagnostic_agent
python -m src.agentic.workflows.healthcare_workflow
python -m utils.simple_healthcare_workflow_demo
```

## 💻 Basic Usage Examples

### Python API Usage
```python
from src.agentic.agents import DiagnosticAgent, SymptomExtractionAgent
from src.agentic.teams import ResearchTestingTeam
from src.agentic.workflows import HealthcareWorkflow

# Use individual agents
symptom_agent = SymptomExtractionAgent()
symptoms = symptom_agent.run("Patient has chest pain and shortness of breath")

diagnostic_agent = DiagnosticAgent()
diagnosis = diagnostic_agent.run(symptoms)

# Use coordinated teams  
team = ResearchTestingTeam()
analysis = team.run("Investigate chest pain symptoms")

# Use full workflow
workflow = HealthcareWorkflow()
result = workflow.run("Patient inquiry about chest pain")
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
pytest src/agentic/agents/diagnostic_agent/tests/
pytest src/agentic/teams/research_testing_team/tests/
pytest src/agentic/workflows/healthcare_workflow/tests/

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
- `src/agentic/workflows/healthcare_workflow/config.py` - Workflow settings
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