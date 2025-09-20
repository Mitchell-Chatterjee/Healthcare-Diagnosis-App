# Shared - Healthcare Diagnosis App

This directory contains shared resources used across different components of the Healthcare Diagnosis App.

## 📁 Structure

```
shared/
├── schemas/              # Common data schemas and models
│   ├── medical.py       # Medical data structures  
│   ├── patient.py       # Patient information schemas
│   └── workflow.py      # Workflow state schemas
├── types/               # Common type definitions
│   ├── enums.py         # Enumerated values
│   └── constants.py     # System constants
├── config/              # Configuration templates
│   ├── base.py          # Base configuration classes
│   └── environments/    # Environment-specific configs
└── utils/               # Cross-component utilities
    ├── validation.py    # Data validation helpers
    └── formatting.py    # Data formatting utilities
```

## 🎯 Purpose

The shared directory provides:

### Common Data Models
- Standardized medical data structures
- Patient information schemas  
- Workflow state definitions
- API request/response models

### Type Definitions
- Medical terminology enums
- Severity levels and classifications
- System-wide constants
- Error codes and messages

### Configuration Management  
- Environment configuration templates
- Feature flags and toggles
- API endpoint definitions
- Default settings and limits

### Utility Functions
- Data validation helpers
- Format conversion utilities
- Common business logic
- Shared error handling

## 🔄 Usage

Import shared resources from any component:

```python
# Use shared schemas
from shared.schemas.medical import DiagnosisResult, TestResult
from shared.schemas.patient import PatientInfo

# Use shared types
from shared.types.enums import SeverityLevel, UrgencyLevel
from shared.types.constants import MAX_SYMPTOMS, DEFAULT_TIMEOUT

# Use shared config
from shared.config.base import BaseConfig
```

## 📊 Cross-Component Standards

This directory ensures consistency across:
- Backend agents and workflows
- API request/response formats  
- Configuration management
- Error handling patterns
- Medical data structures

## 🔧 Maintenance

When adding shared resources:
1. Consider if it's truly cross-component
2. Follow established naming conventions
3. Include comprehensive documentation
4. Add appropriate type hints
5. Update relevant components that could benefit