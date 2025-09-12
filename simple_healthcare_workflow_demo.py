"""
Practical example: Retrofitting the Healthcare Workflow with automatic instrumentation.

This shows how to remove the manual @observe decorators and super() calls
and replace them with automatic instrumentation.
"""

import asyncio
import random
from textwrap import dedent
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.test_utils.plausible_health_scenarios import all_test_scenarios

# STEP 1: Enable automatic instrumentation at the module level
from agno_test.utils.unified_instrumentation import UnifiedInstrumentation, InstrumentationMethod

# Choose your preferred method
instrumentation = UnifiedInstrumentation(InstrumentationMethod.MONKEY_PATCH)
instrumentation.enable()

print("✅ Automatic instrumentation enabled!")

# STEP 2: Define agents/teams WITHOUT any @observe decorators or manual calls
from agno.agent import Agent
from agno.team.team import Team

class SimpleSymptomExtractionAgent(Agent):
    """Symptom extraction agent - NO DECORATORS NEEDED!"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="Simple Symptom Extraction Agent",
            model=mistral_small_32_online(),
            instructions=dedent("""\
                You are a medical symptom extraction specialist.
                Extract and list the specific symptoms mentioned by the patient.
                Be precise and medical in your language.
            """),
            **kwargs
        )
    
    # LOOK: No @observe decorator, just a simple super() call!
    def run(self, message, *args, **kwargs):
        """Run the agent - instrumentation is automatic!"""
        return super().run(message, *args, **kwargs)


class SimpleDiagnosticAgent(Agent):
    """Diagnostic agent - NO DECORATORS NEEDED!"""
    
    def __init__(self, **kwargs):
        super().__init__(
            name="Simple Diagnostic Agent", 
            model=mistral_small_32_online(),
            instructions=dedent("""\
                You are a medical diagnostic specialist.
                Based on symptoms and test results, provide a medical diagnosis.
                Be thorough and evidence-based in your diagnosis.
            """),
            **kwargs
        )
    
    # LOOK: No @observe decorator, no manual test case creation!
    def run(self, message, *args, **kwargs):
        """Run the agent - instrumentation is automatic!"""
        return super().run(message, *args, **kwargs)


class SimpleResearchTestingTeam(Team):
    """Research testing team - NO DECORATORS NEEDED!"""
    
    def __init__(self, **kwargs):
        # For demo purposes, create simple agents for the team
        research_agent = Agent(
            name="Research Agent",
            model=mistral_small_32_online(),
            instructions="Research medical information and recommend tests."
        )
        
        testing_agent = Agent(
            name="Testing Agent", 
            model=mistral_small_32_online(),
            instructions="Run medical tests and provide results."
        )
        
        super().__init__(
            name="Simple Research Testing Team",
            description="A team that coordinates research and testing.",
            mode="coordinate",
            model=mistral_small_32_online(),
            members=[research_agent, testing_agent],
            instructions=dedent("""\
                Coordinate research and testing for medical inquiries.
                Provide comprehensive findings without diagnosis.
            """),
            **kwargs
        )
    
    # LOOK: No @observe decorator, no manual span updates!
    def run(self, message, *args, **kwargs):
        """Run the team - instrumentation is automatic!"""
        return super().run(message, *args, **kwargs)


class SimpleHealthcareWorkflow(Workflow):
    """Healthcare workflow - NO DECORATORS NEEDED!"""

    def __init__(self, use_storage: bool = True):
        """Initialize the simple healthcare workflow."""
        
        # Create agents and team
        symptom_agent = SimpleSymptomExtractionAgent()
        research_testing_team = SimpleResearchTestingTeam()
        diagnostic_agent = SimpleDiagnosticAgent()
        
        # Create steps
        symptom_step = Step(name="Symptom Extraction", agent=symptom_agent)
        research_step = Step(name="Research and Testing", team=research_testing_team)
        diagnosis_step = Step(name="Diagnosis", agent=diagnostic_agent)
        
        # Database setup
        workflow_db_file = "tmp/simple_workflow_storage.db"
        workflow_storage = SqliteStorage(table_name="simple_workflow_storage", db_file=workflow_db_file)
        
        super().__init__(
            name="Simple Healthcare Workflow",
            description="A simplified healthcare workflow with automatic instrumentation",
            storage=workflow_storage if use_storage else None,
            steps=[symptom_step, research_step, diagnosis_step],
            workflow_session_state={},
        )

    # LOOK: No @observe decorator, no manual LLMTestCase creation!
    def run(self, message, *args, **kwargs):
        """Run the workflow - instrumentation is automatic!"""
        return super().run(message, *args, **kwargs)


async def test_simple_healthcare_workflow():
    """Test the simplified healthcare workflow."""
    print("\n" + "=" * 60)
    print("🧪 TESTING SIMPLE HEALTHCARE WORKFLOW")
    print("=" * 60)

    # Create the workflow - no special setup required!
    workflow = SimpleHealthcareWorkflow()
    
    # Select a test scenario
    test_scenario = {
        "user_query": "I've been having chest pain and shortness of breath for the past 2 days. The pain gets worse when I take deep breaths.",
        "diagnosis": "Pleurisy or Pulmonary Embolism"
    }
    
    print(f"🔍 Test Query: {test_scenario['user_query']}")
    print(f"🎯 Expected: {test_scenario['diagnosis']}")
    print("\n" + "-" * 60)

    try:
        # Just run it - all instrumentation happens automatically!
        response = workflow.run(message=test_scenario['user_query'])
        
        print(f"\n✅ Workflow completed successfully!")
        print(f"📊 Response: {response.content[:200]}...")
        
        # The observability data was automatically captured!
        print(f"🔍 All telemetry and evaluation metrics were automatically collected!")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def compare_code_approaches():
    """Show the before/after comparison."""
    print("\n" + "=" * 60)
    print("📊 CODE COMPARISON: BEFORE vs AFTER")
    print("=" * 60)
    
    print("\n🔴 BEFORE (Manual approach):")
    print("-" * 30)
    print("""
@observe(type="workflow", name="Healthcare Workflow", 
         metrics=combine_metrics([correctness_metrics(threshold=0), 
                                 answer_relevancy_metrics(threshold=0.5)]))
def run(self, message, *args, **kwargs):
    response = super().run(message=message, *args, **kwargs)
    expected_output = self.workflow_session_state.get("expected_output", "")
    
    update_current_span(test_case=LLMTestCase(
        input=message, 
        expected_output=expected_output, 
        actual_output=response.content
    ))
    
    return response
    """)
    
    print("\n🟢 AFTER (Automatic approach):")
    print("-" * 30)
    print("""
def run(self, message, *args, **kwargs):
    return super().run(message, *args, **kwargs)
    """)
    
    print(f"\n📈 LINES OF CODE REDUCED: ~10 lines → 2 lines (80% reduction)")
    print(f"🧠 COGNITIVE LOAD: Manual complexity → Simple super() call")
    print(f"🐛 ERROR PRONE: Manual test case creation → Automatic")
    print(f"🔄 MAINTENANCE: Multiple decorators per class → Zero")


async def main():
    """Main demonstration function."""
    print("🚀 AUTOMATIC INSTRUMENTATION DEMO")
    print("=" * 60)
    
    print("\n📋 What this demo shows:")
    print("• How to enable automatic instrumentation")
    print("• Creating agents/teams/workflows WITHOUT decorators")  
    print("• All observability happens automatically")
    print("• Massive reduction in boilerplate code")
    
    # Show the code comparison
    compare_code_approaches()
    
    # Test the simple workflow
    await test_simple_healthcare_workflow()
    
    print("\n" + "=" * 60)
    print("🎉 DEMO COMPLETE")
    print("=" * 60)
    print("\n💡 Key Takeaway:")
    print("   New developers just need to write super().run() - that's it!")
    print("   All observability, metrics, and evaluation happens automatically.")


if __name__ == "__main__":
    asyncio.run(main())
