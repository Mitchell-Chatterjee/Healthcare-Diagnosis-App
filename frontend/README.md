# Healthcare Diagnosis App - Streamlit Frontend

A modern, interactive web interface for the Healthcare Diagnosis App built with Streamlit, leveraging Agno's powerful AI agent capabilities for medical analysis.

## 🎯 Overview

This Streamlit frontend provides an intuitive, user-friendly interface for healthcare professionals and researchers to interact with our AI-powered diagnostic system. It seamlessly integrates with the backend's agentic AI components to deliver real-time medical insights.

## 🏗️ Architecture

```
frontend/
├── src/
│   ├── app.py                 # Main Streamlit application
│   ├── pages/                 # Multi-page application
│   │   ├── 01_symptom_analysis.py
│   │   ├── 02_diagnostic_workflow.py
│   │   ├── 03_research_insights.py
│   │   ├── 04_test_recommendations.py
│   │   └── 05_team_collaboration.py
│   ├── components/            # Reusable UI components
│   │   ├── __init__.py
│   │   ├── agent_interface.py
│   │   ├── diagnosis_display.py
│   │   ├── medical_forms.py
│   │   └── result_visualization.py
│   ├── services/             # Backend API integration
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   └── agentic_client.py
│   └── utils/                # Frontend utilities
│       ├── __init__.py
│       ├── session_state.py
│       ├── medical_validators.py
│       └── ui_helpers.py
├── assets/                   # Static assets
│   ├── images/
│   ├── styles/
│   │   └── main.css
│   └── icons/
├── config/
│   ├── app_config.py
│   └── streamlit_config.toml
├── requirements.txt          # Frontend dependencies
├── Dockerfile               # Container configuration
└── README.md               # This file
```

## ✨ Key Features

### 🤖 AI-Powered Interfaces
- **Interactive Agent Chat**: Real-time conversations with individual AI agents
- **Team Collaboration View**: Watch multiple agents collaborate on complex cases
- **Workflow Visualization**: Step-by-step diagnostic process visualization
- **Research Integration**: Live medical research and evidence display

### 📊 Rich Visualizations
- **Symptom Mapping**: Interactive body diagrams for symptom location
- **Confidence Metrics**: Real-time confidence scoring for diagnoses
- **Research Evidence**: Citation networks and evidence strength visualization
- **Test Result Interpretation**: Interactive charts and medical imagery

### 🩺 Healthcare-Specific UI
- **HIPAA-Compliant Design**: Privacy-first interface design
- **Medical Terminology**: Proper medical term display and tooltips
- **Clinical Decision Support**: Clear recommendation presentations
- **Audit Trail**: Complete interaction logging for medical records

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Access to Healthcare Diagnosis App backend
- Streamlit 1.28+

### Installation

```bash
cd frontend

# Create virtual environment
python -m venv streamlit-env
source streamlit-env/bin/activate  # On Windows: streamlit-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create configuration file:
```bash
cp config/app_config.py.example config/app_config.py
```

2. Configure backend connection:
```python
# config/app_config.py
BACKEND_URL = "http://localhost:8000"
API_VERSION = "v1"
AGENTIC_ENDPOINT = "/agentic"

# Authentication (if enabled)
API_KEY = "your-api-key"
JWT_SECRET = "your-jwt-secret"
```

### Running the App

```bash
# Development mode
streamlit run src/app.py

# Production mode with custom config
streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0
```

## 🎨 Pages & Components

### Main Dashboard (`src/app.py`)
- **Patient Intake Form**: Structured data collection
- **Quick Diagnosis**: Fast symptom-to-diagnosis pipeline
- **Agent Status**: Live status of all AI agents
- **Recent Cases**: Case history and patterns

### Symptom Analysis (`pages/01_symptom_analysis.py`)
```python
# Interactive symptom extraction
symptom_agent = AgenticClient().get_symptom_extraction_agent()

# Real-time symptom processing
with st.chat_message("assistant"):
    symptoms = st.session_state.symptom_agent.process(
        user_input=patient_description,
        stream=True
    )
    
# Structured symptom display
display_extracted_symptoms(symptoms)
```

### Diagnostic Workflow (`pages/02_diagnostic_workflow.py`)
```python
# Complete workflow visualization
workflow = AgenticClient().get_healthcare_workflow()

# Step-by-step execution with progress
progress_bar = st.progress(0)
for step_num, step_result in enumerate(workflow.run_with_progress(patient_data)):
    progress_bar.progress((step_num + 1) / workflow.total_steps)
    display_workflow_step(step_result)
```

### Research Insights (`pages/03_research_insights.py`)
```python
# Live research integration
research_agent = AgenticClient().get_research_agent()

# Interactive research queries
research_query = st.text_input("Research Topic")
if research_query:
    with st.spinner("Searching medical literature..."):
        evidence = research_agent.search(research_query)
    
    # Rich evidence display
    display_research_evidence(evidence)
    show_citation_network(evidence.citations)
```

### Team Collaboration (`pages/05_team_collaboration.py`)
```python
# Multi-agent team interface
team = AgenticClient().get_research_testing_team()

# Real-time collaboration view
col1, col2, col3 = st.columns(3)
with col1:
    display_agent_status("Research Agent", team.research_agent)
with col2:
    display_agent_status("Testing Agent", team.testing_agent)
with col3:
    display_agent_status("Diagnostic Agent", team.diagnostic_agent)

# Collaborative analysis
team_result = team.analyze_case(case_data)
display_team_consensus(team_result)
```

## 🛠️ Agno Integration

### Agent Client (`services/agentic_client.py`)
```python
import requests
from typing import Dict, Any, Generator

class AgenticClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get_diagnostic_agent(self):
        """Get DiagnosticAgent proxy for Streamlit"""
        return AgentProxy(self, "diagnostic")
    
    def get_symptom_extraction_agent(self):
        """Get SymptomExtractionAgent proxy"""
        return AgentProxy(self, "symptom_extraction")
    
    def stream_workflow(self, workflow_id: str, data: Dict[str, Any]) -> Generator:
        """Stream workflow execution for real-time updates"""
        response = self.session.post(
            f"{self.base_url}/agentic/workflows/{workflow_id}/stream",
            json=data,
            stream=True
        )
        
        for line in response.iter_lines():
            if line:
                yield json.loads(line)
```

### Real-time Updates with Agno Streaming
```python
# Stream diagnostic process
def stream_diagnosis():
    workflow = AgenticClient().get_healthcare_workflow()
    
    # Create real-time display containers
    status_container = st.empty()
    results_container = st.empty()
    
    for update in workflow.stream_execution(patient_data):
        # Update status
        status_container.info(f"Step: {update.current_step}")
        
        # Update results as they come in
        if update.partial_result:
            results_container.write(update.partial_result)
    
    # Final results
    results_container.success("Diagnosis complete!")
```

## 🎯 UI/UX Features

### Medical-Specific Components
```python
# Medical timeline component
def display_medical_timeline(events):
    for event in events:
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write(event.timestamp)
            with col2:
                st.info(f"**{event.type}**: {event.description}")

# Interactive body diagram
def body_diagram_selector():
    # SVG-based body diagram with click regions
    body_svg = load_body_diagram()
    selected_regions = st_clickable_images(
        body_svg, 
        key="body_regions",
        click_mode="multi"
    )
    return selected_regions

# Medical confidence display
def show_confidence_meter(confidence: float, explanation: str):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("Confidence", f"{confidence:.1%}")
    with col2:
        st.progress(confidence)
        st.caption(explanation)
```

### Advanced Visualizations
```python
import plotly.graph_objects as go
import plotly.express as px

def create_symptom_network(symptoms):
    """Interactive symptom relationship network"""
    fig = go.Figure(data=go.Scatter(
        x=[s.x for s in symptoms],
        y=[s.y for s in symptoms],
        mode='markers+text',
        text=[s.name for s in symptoms],
        textposition="middle center"
    ))
    
    # Add connections between related symptoms
    for connection in symptom_connections:
        fig.add_trace(go.Scatter(
            x=[connection.start.x, connection.end.x],
            y=[connection.start.y, connection.end.y],
            mode='lines',
            line=dict(width=connection.strength * 5)
        ))
    
    return fig

def research_evidence_chart(evidence):
    """Evidence strength visualization"""
    fig = px.bar(
        evidence, 
        x='study_type', 
        y='evidence_level',
        color='confidence',
        title="Research Evidence Strength"
    )
    return fig
```

## 🔒 Security & Compliance

### HIPAA Compliance Features
- **No Local Storage**: Patient data never stored in browser
- **Session Encryption**: All data encrypted in transit
- **Access Logging**: Complete audit trail of user interactions
- **Role-Based Access**: Different interfaces for different user types

### Privacy Protection
```python
# Data sanitization
def sanitize_display_data(medical_data):
    """Remove/mask PII from display data"""
    sanitized = medical_data.copy()
    
    # Mask patient identifiers
    sanitized.patient_id = mask_identifier(sanitized.patient_id)
    sanitized.patient_name = "[Patient Name Hidden]"
    
    return sanitized

# Session management
def init_secure_session():
    """Initialize secure session state"""
    if 'session_token' not in st.session_state:
        st.session_state.session_token = generate_session_token()
        st.session_state.user_role = authenticate_user()
        st.session_state.permissions = get_user_permissions()
```

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY config/ ./config/
COPY assets/ ./assets/

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py", "--server.address", "0.0.0.0"]
```

### Production Configuration
```toml
# config/streamlit_config.toml
[server]
port = 8501
address = "0.0.0.0"
maxUploadSize = 200

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"

[browser]
gatherUsageStats = false
```

## 🧪 Testing

```bash
# Run frontend tests
pytest tests/

# Test API integration
pytest tests/test_api_integration.py

# UI component tests
pytest tests/test_components.py

# End-to-end tests
playwright test
```

## 📈 Features Roadmap

### Phase 1 - Core Interface
- [x] Basic patient intake forms
- [x] Individual agent interactions
- [x] Simple diagnostic display
- [x] Real-time agent status

### Phase 2 - Advanced Features
- [ ] Interactive body diagrams
- [ ] Multi-agent collaboration view
- [ ] Research evidence visualization
- [ ] Medical timeline display

### Phase 3 - Enterprise Features
- [ ] Role-based dashboards
- [ ] Advanced analytics
- [ ] Integration with EHR systems
- [ ] Mobile-responsive design

### Phase 4 - AI Enhancement
- [ ] Voice input/output
- [ ] Medical image upload
- [ ] Predictive analytics
- [ ] Custom agent training interface

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/streamlit-enhancement`)
3. Commit your changes (`git commit -am 'Add new medical visualization'`)
4. Push to the branch (`git push origin feature/streamlit-enhancement`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Medical Disclaimer**: This interface is for healthcare professional use and research purposes only. Always follow appropriate medical guidelines and consult with qualified healthcare providers.