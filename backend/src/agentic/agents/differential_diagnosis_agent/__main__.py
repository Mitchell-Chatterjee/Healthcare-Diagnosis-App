#!/usr/bin/env python3

import sys
from pathlib import Path

# Add the backend src directory to Python path
backend_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(backend_root))

from agentic.agents.differential_diagnosis_agent.agent import DifferentialDiagnosisAgent

if __name__ == "__main__":
    agent = DifferentialDiagnosisAgent()
    
    # Simple but comprehensive test case
    test_query = """
    I'm a 52-year-old man and I just came to the emergency room because I'm having severe chest pain 
    that started about 30 minutes ago while I was climbing stairs at work. The pain feels like someone 
    is crushing my chest and it's going down my left arm and up to my jaw. I'm sweating a lot and feel 
    really anxious. I have high blood pressure and I've been smoking for about 25 years. I take 
    lisinopril but honestly I haven't been great about taking it regularly lately. What could be 
    causing this pain and what should the doctors be looking for?
    """
    
    response = agent.print_response(test_query.strip())