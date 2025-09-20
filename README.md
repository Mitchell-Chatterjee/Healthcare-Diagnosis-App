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
│   │   ├── agentic/         # 🧠 All AI/LLM-powered components
│   │   │   ├── agents/      # Individual AI healthcare agents
│   │   │   ├── teams/       # Multi-agent collaboration teams
│   │   │   ├── workflows/   # AI-powered diagnostic workflows
│   │   │   └── tools/       # Agent-specific tools & integrations
│   │   ├── api/             # REST API endpoints
│   │   ├── services/        # Business logic layer
│   │   └── common/          # Shared utilities & configuration
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

The AI components are organized under `backend/src/agentic/` for clear separation between intelligent AI functionality and traditional backend services.

### Core Agents (`backend/src/agentic/agents/`)
Specialized AI agents for medical tasks:

- **SymptomExtractionAgent**: Extracts and structures symptoms from patient inquiries
- **MedicalResearchAgent**: Conducts medical research using search capabilities
- **MedicalTestAgent**: Coordinates and executes diagnostic tests
- **DiagnosticAgent**: Provides diagnostic analysis based on symptoms and test results

### Collaborative Teams (`backend/src/agentic/teams/`)
Multi-agent coordination for complex medical analysis:

- **ResearchTestingTeam**: Coordinates research and testing agents for comprehensive medical evaluation

### Complete Workflows (`backend/src/agentic/workflows/`)
End-to-end AI-powered diagnostic processes:

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
from src.agentic.agents import DiagnosticAgent, SymptomExtractionAgent

# Extract symptoms from patient inquiry
symptom_agent = SymptomExtractionAgent()
symptoms = symptom_agent.run("I have chest pain and shortness of breath")

# Perform diagnostic analysis
diagnostic_agent = DiagnosticAgent()
diagnosis = diagnostic_agent.run(patient_data)
```

#### Team Coordination
```python
from src.agentic.teams import ResearchTestingTeam

# Use coordinated research and testing
team = ResearchTestingTeam()
analysis = team.run("Investigate chest pain and breathing difficulty")
```


#### Complete Workflows
```python
from src.agentic.workflows import HealthcareWorkflow

# Run complete diagnostic workflow
workflow = HealthcareWorkflow()
result = workflow.run(patient_inquiry)
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
backend/src/agentic/workflows/workflow_name/
├── __init__.py         # Package exports: Workflow class and functions
├── __main__.py         # Entry point for standalone execution
├── workflow.py         # Main workflow implementation
# Healthcare Diagnosis App

Lightweight monorepo for research and development of an AI-assisted healthcare diagnosis system.

This repository contains two main components:

- `backend/` — Python backend with AI agents, teams, and workflows. See `backend/README.md` for setup, virtual environment instructions, and developer docs.
- `frontend/` — Streamlit frontend for interacting with the agents. See `frontend/README.md` for frontend setup and usage.

Quick pointers

- Python: 3.9+
- Backend virtualenv (recommended): `backend/uv` (see `backend/README.md` for activation commands)
- For contribution and development workflows, follow the per-component READMEs.

For full project documentation, developer guides, and API details, open the component READMEs or the `docs/` directory.

License: MIT — see `LICENSE`.
