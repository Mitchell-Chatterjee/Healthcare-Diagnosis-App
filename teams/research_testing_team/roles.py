def define_team_roles():
    """Define how agents collaborate within the Research Testing Team."""
    return {
        "lead": "Medical Research Agent",        # Primary research coordinator
        "executor": "Medical Test Agent",        # Test execution specialist
        "coordination_mode": "coordinate",       # Sequential coordination
        "communication_pattern": "research_first_then_test"
    }

def get_workflow_phases():
    """Define the workflow phases for the team."""
    return [
        "research_phase",      # Medical Research Agent conducts research
        "testing_phase",       # Medical Test Agent executes tests  
        "iterative_phase",     # Repeat research/testing if needed
        "summary_phase"        # Compile comprehensive findings
    ]

def get_coordination_rules():
    """Define coordination rules between team members."""
    return {
        "start_with_research": True,
        "ensure_context_passing": True,
        "iterate_until_complete": True,
        "no_diagnostic_conclusions": True,
        "focus_on_data_gathering": True
    }
