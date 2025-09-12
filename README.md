# Iris API Development Guide

This guide defines the standard structure and patterns for developing new agents, teams, and workflows in the Iris Agentic system.

> ⚠️ **Security Notice**: Before using this package, please review the [SECURITY.md](./SECURITY.md) file for important information about API keys and secure configuration.

## 🏗️ Component Types Overview

### **Agents** (`agents/`)
Individual AI agents that perform specific, focused tasks. Each agent is self-contained and can be used independently or as part of workflows.

**Examples**: Content alignment, general knowledge, document analysis, data extraction

### **Teams** (`teams/`)
Collections of agents that collaborate to solve complex problems. Teams coordinate multiple agents with shared context and goal-oriented collaboration.

**Examples**: Research teams, analysis teams, multi-step processing teams

### **Workflows** (`workflows/`)
Orchestration logic that defines the flow of data and decisions between agents, teams, and processing steps. Workflows can be linear, branched, or conditional.

**Examples**: Content processing pipelines, approval workflows, multi-stage analysis

### **Common** (`common/`)
Shared utilities, models, configurations, and base classes used across all components.

## 📦 Standard Package Structure

### Agent Package Structure
```
agents/my_agent/
├── __init__.py         # Package exports: Agent class and schemas
├── __main__.py         # Entry point for standalone execution  
├── agent.py            # Main agent class implementation
├── schemas.py          # Pydantic models for input/output (optional)
├── prompts.py          # Agent descriptions, instructions, examples
├── tools.py            # Custom tools specific to this agent (optional)
├── config.py           # Agent-specific configuration (optional)
└── tests/              # Unit tests for the agent (optional)
    ├── __init__.py
    ├── test_agent.py
    └── test_schemas.py
```

### Team Package Structure
```
teams/my_team/
├── __init__.py         # Package exports: Team class and schemas
├── __main__.py         # Entry point for standalone execution
├── team.py             # Main team orchestration class
├── schemas.py          # Team-specific data models (optional)
├── roles.py            # Agent role definitions and assignments
├── coordination.py     # Team collaboration logic (optional)
├── config.py           # Team configuration and settings (optional)
└── tests/              # Unit tests for the team (optional)
    ├── __init__.py
    ├── test_team.py
    └── test_coordination.py
```

### Workflow Package Structure
```
workflows/my_workflow/
├── __init__.py         # Package exports: Workflow class and functions
├── __main__.py         # Entry point for standalone execution
├── workflow.py         # Main workflow implementation
├── schemas.py          # Workflow-specific data models (optional)
├── steps.py            # Individual step functions (optional)
├── routing.py          # Conditional routing logic (optional)
├── gates.py            # Decision gates and filters (optional)
├── config.py           # Workflow configuration (optional)
└── tests/              # Unit tests for the workflow (optional)
    ├── __init__.py
    ├── test_workflow.py
    └── test_steps.py
```

## 🛠️ Development Patterns

### Creating a New Agent

#### 1. **Create the Package Structure**
```bash
mkdir -p agents/my_agent/tests
touch agents/my_agent/{__init__.py,__main__.py,agent.py,prompts.py}
```

#### 2. **Implement the Agent** (`agent.py`)
```python
from agno.agent import Agent
from iris.api.common.models import mistral_small_32
from .prompts import my_agent_description, my_agent_instructions
from .schemas import MyAgentResponse  # optional

class MyAgent(Agent):
    """Brief description of what this agent does."""
    
    def __init__(self, name: str = "My Agent", **kwargs):
        super().__init__(
            name=name,
            model=mistral_small_32(),
            description=my_agent_description,
            instructions=my_agent_instructions,
            response_model=MyAgentResponse,  # optional
            **kwargs
        )
```

#### 3. **Define Prompts** (`prompts.py`)
```python
my_agent_description = """
Clear, concise description of the agent's purpose and capabilities.
Focus on what it does, not how it does it.
"""

my_agent_instructions = [
    "Primary instruction or rule",
    "Secondary behavioral guideline", 
    "Output format specification",
    "Any constraints or limitations"
]
```

#### 4. **Create Schemas** (`schemas.py`) - Optional
```python
from pydantic import BaseModel, Field
from typing import Optional

class MyAgentRequest(BaseModel):
    """Input schema for the agent."""
    query: str = Field(..., description="The user's request")
    context: Optional[str] = Field(None, description="Additional context")

class MyAgentResponse(BaseModel):
    """Output schema for the agent."""
    result: str = Field(..., description="The agent's response")
    confidence: float = Field(..., description="Confidence score 0-1")
```

#### 5. **Package Exports** (`__init__.py`)
```python
from .agent import MyAgent
from .schemas import MyAgentRequest, MyAgentResponse  # if applicable

__all__ = ["MyAgent", "MyAgentRequest", "MyAgentResponse"]
```

#### 6. **Entry Point** (`__main__.py`)
```python
#!/usr/bin/env python3
from iris.api.agents.my_agent import MyAgent

if __name__ == "__main__":
    agent = MyAgent()
    response = agent.run("Test query")
    print(response)
```

### Creating a New Team

#### 1. **Team Implementation** (`team.py`)
```python
from agno.team import Team
from iris.api.agents.agent_a import AgentA
from iris.api.agents.agent_b import AgentB
from .roles import define_team_roles
from .schemas import TeamResponse

class MyTeam(Team):
    """Team that coordinates multiple agents for complex tasks."""
    
    def __init__(self, **kwargs):
        agents = [AgentA(), AgentB()]
        super().__init__(
            name="My Team",
            agents=agents,
            roles=define_team_roles(),
            **kwargs
        )
```

#### 2. **Role Definitions** (`roles.py`)
```python
def define_team_roles():
    """Define how agents collaborate within the team."""
    return {
        "lead": "AgentA",      # Primary decision maker
        "analyst": "AgentB",   # Data analysis role
        # Add coordination rules, communication patterns, etc.
    }
```

### Creating a New Workflow

#### 1. **Workflow Implementation** (`workflow.py`)
```python
from agno.workflow.v2 import Workflow, Step
from iris.api.agents.my_agent import MyAgent
from iris.api.teams.my_team import MyTeam
from .steps import custom_processing_step

class MyWorkflow(Workflow):
    """Workflow that orchestrates a multi-step process."""
    
    def __init__(self):
        super().__init__(
            name="My Workflow",
            description="Description of the workflow's purpose",
            steps=[
                Step(name="Initial Processing", agent=MyAgent()),
                Step(name="Team Analysis", team=MyTeam()),
                Step(name="Custom Step", executor=custom_processing_step),
            ]
        )
```

#### 2. **Custom Steps** (`steps.py`)
```python
from agno.workflow.v2 import StepInput, StepOutput

def custom_processing_step(step_input: StepInput) -> StepOutput:
    """Custom processing logic for workflow steps."""
    # Process the input from previous step
    result = process_data(step_input.previous_step_content)
    
    return StepOutput(
        content=result,
        stop=False  # Continue to next step
    )
```

## 🔄 Integration Guidelines

### 1. **Update Main Package Exports**
After creating a new component, update the main package `__init__.py`:

```python
# In agents/__init__.py
from .my_agent import MyAgent
# Add to __all__ list

# In teams/__init__.py  
from .my_team import MyTeam
# Add to __all__ list

# In workflows/__init__.py
from .my_workflow import MyWorkflow
# Add to __all__ list
```

### 2. **Add Debug Configuration**
Update `.vscode/launch.json` with a new debug configuration:

```json
{
  "name": "Python: Debug my_agent",
  "type": "debugpy", 
  "request": "launch",
  "module": "iris.api.agents.my_agent",
  "console": "integratedTerminal",
  "cwd": "${workspaceFolder}/src"
}
```

### 3. **Running Components**
```bash
# Run as module
uv run python -m iris.api.agents.my_agent
uv run python -m iris.api.teams.my_team  
uv run python -m iris.api.workflows.my_workflow
```

## 📋 Naming Conventions

- **Packages**: `snake_case` (e.g., `content_analyzer`, `research_team`)
- **Classes**: `PascalCase` (e.g., `ContentAnalyzer`, `ResearchTeam`) 
- **Files**: `snake_case.py` (e.g., `agent.py`, `schemas.py`)
- **Functions**: `snake_case` (e.g., `process_content`, `analyze_data`)

## 🎯 Best Practices

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Loose Coupling**: Minimize dependencies between components
3. **Clear Interfaces**: Use Pydantic schemas for complex inputs/outputs
4. **Documentation**: Include docstrings and clear descriptions
5. **Testing**: Provide unit tests for complex logic
6. **Configuration**: Use config files for environment-specific settings
7. **Error Handling**: Implement proper error handling and logging

## 🔮 Future Component Types
## 🧭 Workflow instantiation & dependency injection

- Recommended: instantiate a new Workflow per incoming request/session to keep `workflow_session_state` isolated and avoid cross-request leakage or races.
- Agno is optimized for fast workflow/agent instantiation; the real costs are model inference and external clients (DBs, vectordbs, network I/O).
- Avoid recreating heavy resources per-request. Reuse them via module-level singletons or an explicit factory/DI pattern (inject shared models, DB clients, and agents into per-request workflow instances).
- If you must reuse the same Workflow/Agent instances concurrently, implement safe merging or locking (or operate on a per-run copy of session state) to prevent overwrites.
- Keep persisted session state small and JSON-serializable (store only fields you need, e.g. `language` or `session_scope_filter`) to simplify merging and persistence.


## Using workflow session state (blackboard pattern)

Treat the per-run `workflow_session_state` dict as a lightweight blackboard via `WorkflowStateAdapter`.
Store Pydantic models with `store_object` (uses `model_dump`) and reconstruct with `get_object` (uses `model_validate`).
Helpers: `has_object`, `remove_object`.
Keep class names unique for keys, keep stored data small, and instantiate a fresh workflow/session per request to avoid cross-run leakage.

### Closure-based access (recommended)

Capture the workflow session dict in a router factory instead of passing it through `additional_data`.

```py
def create_router_selector(session_state: dict):
    def selector(step_input):
        req = WorkflowStateAdapter.get_object(session_state, IrisRequest)
        return [general_knowledge_pipeline]
    return selector

# pass the same dict into the router when building the Workflow
workflow_session_state = {}
steps = [..., create_iris_pipeline_router(workflow_session_state)]
```



### **Monitors** (`monitors/`)
Components that observe and report on system behavior, agent performance, and workflow metrics.

### **Adapters** (`adapters/`)
Interface components that connect external systems, APIs, or data sources to the Iris ecosystem.

### **Policies** (`policies/`)
Configurable rule sets that govern agent behavior, content filtering, and access control.

### **Schedulers** (`schedulers/`)
Components that manage time-based execution, background tasks, and workflow scheduling.