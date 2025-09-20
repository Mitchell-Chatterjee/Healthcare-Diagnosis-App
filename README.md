# Healthcare Diagnosis App

An AI-powered healthcare diagnosis assistance system built with Python and the Agno framework. This application provides intelligent medical analysis through coordinated AI agents, teams, and workflows.

> ⚠️ **Important Medical Disclaimer**: This system provides information for educational purposes only and is not intended as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

> 🔒 **Security Notice**: Please review [SECURITY.md](./SECURITY.md) for important information about API keys and secure configuration.

## 🏗️ Repository Structure

This is a **monorepo** organized into focused directories:

```
Healthcare-Diagnosis-App/
├── backend/                   # Python backend with AI agents & workflows
│   ├── src/                  # All source code
│   │   ├── agents/          # Individual AI healthcare agents
│   │   ├── teams/           # Multi-agent collaboration teams
│   │   ├── workflows/       # End-to-end diagnostic workflows
│   │   ├── api/             # REST API endpoints
│   │   ├── services/        # Business logic layer
│   │   ├── common/          # Shared utilities & configuration
│   │   └── tools/           # Custom medical tools & integrations
│   ├── utils/               # Development utilities & demos
│   └── tests/               # Test infrastructure & shared fixtures
├── shared/                   # Cross-component resources
│   ├── schemas/             # Common data models (medical, patient)
│   ├── types/               # Enums, constants, type definitions
│   ├── config/              # Configuration templates
│   └── utils/               # Shared utility functions
├── docs/                    # Documentation & guides
├── scripts/                 # Build, deployment & utility scripts
├── README.md               # This file
├── LICENSE                 # License information
└── SECURITY.md             # Security guidelines
```

## 🤖 Healthcare AI System

### Core Agents (`backend/src/agents/`)
Specialized AI agents for medical tasks:

- **SymptomExtractionAgent**: Extracts and structures symptoms from patient inquiries
- **MedicalResearchAgent**: Conducts medical research using search capabilities
- **MedicalTestAgent**: Coordinates and executes diagnostic tests
- **DiagnosticAgent**: Provides diagnostic analysis based on symptoms and test results

### Collaborative Teams (`backend/src/teams/`)
Multi-agent coordination for complex medical analysis:

- **ResearchTestingTeam**: Coordinates research and testing agents for comprehensive medical evaluation

### Complete Workflows (`backend/src/workflows/`)
End-to-end diagnostic processes:

- **HealthcareWorkflow**: Complete diagnostic workflow from symptom intake to final diagnosis with research and testing phases

## � Quick Start

### Prerequisites
- Python 3.9+
- pip or uv package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/Mitchell-Chatterjee/Healthcare-Diagnosis-App.git
cd Healthcare-Diagnosis-App

# Install backend dependencies
cd backend
pip install -r requirements.txt
# or with uv
uv install
```

### Basic Usage

#### Individual Agents
```python
from backend.src.agents import DiagnosticAgent, SymptomExtractionAgent

# Extract symptoms from patient inquiry
symptom_agent = SymptomExtractionAgent()
symptoms = symptom_agent.run("I have chest pain and shortness of breath")

# Perform diagnostic analysis
diagnostic_agent = DiagnosticAgent()
diagnosis = diagnostic_agent.run(patient_data)
```

#### Team Coordination
```python
from backend.src.teams import ResearchTestingTeam

# Use coordinated research and testing
team = ResearchTestingTeam()
analysis = team.run("Investigate chest pain and breathing difficulty")
```


#### Complete Workflow
```python
from backend.src.workflows import HealthcareWorkflow

# Run complete diagnostic workflow
workflow = HealthcareWorkflow()
result = workflow.run("Patient inquiry about chest pain")
```

### Running Demos
```bash
# Simple workflow demonstration
cd backend
python -m utils.simple_healthcare_workflow_demo

# Individual agent testing
python -m src.agents.diagnostic_agent
python -m src.agents.medical_research_agent
```

## 📦 Standard Package Structure

All backend components follow consistent structure patterns:

### Agent Package Structure
```
backend/src/agents/agent_name/
├── __init__.py         # Package exports: Agent class and schemas
├── __main__.py         # Entry point for standalone execution  
├── agent.py            # Main agent class implementation
├── schemas.py          # Pydantic models for input/output
├── prompts.py          # Agent descriptions, instructions, examples
└── tests/              # Unit tests for the agent
    ├── __init__.py
    ├── test_agent.py
    └── test_schemas.py
```

### Team Package Structure
```
backend/src/teams/team_name/
├── __init__.py         # Package exports: Team class and schemas
├── __main__.py         # Entry point for standalone execution
├── team.py             # Main team orchestration class
├── roles.py            # Agent role definitions and assignments
├── coordination.py     # Team collaboration logic
├── schemas.py          # Team-specific data models
└── tests/              # Unit tests for the team
    ├── __init__.py
    ├── test_team.py
    └── test_schemas.py
```

### Workflow Package Structure
```
backend/src/workflows/workflow_name/
├── __init__.py         # Package exports: Workflow class and functions
├── __main__.py         # Entry point for standalone execution
├── workflow.py         # Main workflow implementation
├── steps.py            # Individual step functions
├── config.py           # Workflow configuration
├── schemas.py          # Workflow-specific data models
└── tests/              # Unit tests for the workflow
    ├── __init__.py
    ├── test_workflow.py
    └── test_schemas.py
```

## 🛠️ Development

### Running Tests
```bash
# Run all tests
cd backend
pytest

# Run specific component tests
pytest src/agents/diagnostic_agent/tests/
pytest src/teams/research_testing_team/tests/
pytest src/workflows/healthcare_workflow/tests/

# Run with coverage
pytest --cov=src
```

### Code Quality
```bash
# Format code
black backend/src/ backend/utils/ backend/tests/

# Lint code  
flake8 backend/src/ backend/utils/ backend/tests/

# Type checking
mypy backend/src/
```

### Creating New Components

Follow the established patterns in \`backend/src/\` for consistency:

1. **Create Package Structure**: Use standard directory layout
2. **Implement Core Logic**: Follow existing agent/team/workflow patterns
3. **Add Schemas**: Define Pydantic models for inputs/outputs
4. **Write Tests**: Include comprehensive test coverage
5. **Update Exports**: Add to relevant \`__init__.py\` files

## 🔧 Configuration

### Environment Variables
```bash
# Model configuration
HEALTHCARE_MODEL_PROVIDER=openai
HEALTHCARE_API_KEY=your-api-key
HEALTHCARE_MODEL_NAME=gpt-4

# Logging
HEALTHCARE_LOG_LEVEL=INFO
```

### Shared Configuration
The \`shared/\` directory provides cross-component resources:
- Common data schemas and models
- Type definitions and constants
- Base configuration classes
- Shared utility functions

## 🏥 Medical Safety Features

- **Medical Disclaimers**: Automatic medical disclaimer requirements
- **Confidence Scoring**: All diagnoses include confidence levels
- **Emergency Detection**: Automatic detection of emergency symptoms
- **Audit Trails**: Complete logging of medical decisions
- **Professional Review**: Integration points for healthcare provider oversight

## 📚 Documentation

- [Backend README](backend/README.md) - Detailed backend documentation
- [Shared Resources Guide](shared/README.md) - Cross-component resources
- [SECURITY.md](SECURITY.md) - Security and compliance guidelines
- [LICENSE](LICENSE) - License information

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

See [LICENSE](LICENSE) and [SECURITY.md](SECURITY.md) for details.

## 🆘 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the documentation in the \`docs/\` directory
- Check the \`backend/README.md\` for technical details

---

**Remember**: This system is for educational and assistance purposes only. Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment decisions.
