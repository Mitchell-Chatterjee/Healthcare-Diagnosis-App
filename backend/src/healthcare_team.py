import asyncio
from textwrap import dedent
from agno.team.team import Team
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

from agno_test.utils.models import mistral_small_32_online
from agno_test.agents.healthcare.agents.research.research_agent import MedicalResearchAgent
from agno_test.agents.healthcare.agents.medical_test.medical_test_agent import MedicalTestAgent
from agno_test.agents.healthcare.test_utils.utils.eval_metrics import contextual_relevancy_metrics
from agno_test.agents.healthcare.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedTeam

# Database file for Research Testing Team memory and storage
research_testing_db_file = "tmp/research_testing_team.db"
research_testing_storage = SqliteStorage(table_name="research_testing_sessions", db_file=research_testing_db_file)
research_testing_memory = Memory(
    # Use any model for creating memories
    model=mistral_small_32_online(),
    db=SqliteMemoryDb(table_name="research_testing_memories", db_file=research_testing_db_file),
)


class ResearchTestingTeam(InstrumentedTeam):
    """
    A team that coordinates research and testing agents to handle complex medical inquiries.
    """

    def __init__(self, **kwargs):
        """
        Initialize the Research Testing Team.
        
        Args:
            **kwargs: Additional arguments passed to the base Team class
        """
        super().__init__(
            name="Research Testing Team",
            description="A team that coordinates research and testing agents to handle complex medical inquiries.",
            mode="coordinate",
            team_id="research_testing_team",
            model=mistral_small_32_online(),
            members=[
                MedicalResearchAgent(name="Medical Research Agent"),
                MedicalTestAgent(name="Healthcare Test Agent")
            ],
            instructions=dedent("""\
                You are a coordinating team with two specialized members focused on RESEARCH and TESTING ONLY:
                
                1. **Medical Research Agent** - Conducts research using Google to recommend tests
                2. **Healthcare Test Agent** - Orders and runs medical tests based on research findings
                
                CRITICAL: Your role is to gather information and test results, NOT to provide diagnoses or prognoses.
                
                WORKFLOW:
                1. RESEARCH PHASE: Use Medical Research Agent to research symptoms and recommend appropriate tests
                2. TESTING PHASE: Use Healthcare Test Agent to run recommended tests and get results
                3. ITERATIVE PHASE: If results indicate further research or additional tests are needed, repeat the research and testing phases as necessary.
                4. CONCLUDE with a comprehensive summary of findings ONLY
                
                COORDINATION RULES:
                - Always start with research before testing
                - Ensure each agent receives proper context from previous steps
                - Continue iterating between research and testing until you are confident all necessary actions have been taken
                - DO NOT make diagnostic conclusions or suggest specific diagnoses
                
                TASK ROUTING:
                - User health inquiry → Medical Research Agent
                - Research findings → Healthcare Test Agent
                - Test results → Medical Research Agent (if further research is needed)
                - Repeat as needed until all relevant research and tests are complete
                
                OUTPUT REQUIREMENTS:
                Your final response must be a structured summary containing these sections:
                
                **Original Patient Inquiry:**
                [Include the original patient inquiry/symptoms as presented]
                
                **Extracted Symptoms:**
                [List of specific symptoms identified from the inquiry]
                
                **Research Findings:**
                [Key information discovered during research]
                
                **Tests Performed:**
                [List of all tests ordered and executed]
                
                **Test Results:**
                [Actual results from each test]
                
                **Additional Observations:**
                [Any relevant findings that emerged during research/testing]
                
                DO NOT INCLUDE:
                - Diagnostic conclusions
                - Treatment recommendations  
                - Prognosis statements
                - Medical advice
                
                Leave all diagnostic interpretation for the dedicated diagnostic agent in the next stage.
                Focus solely on providing comprehensive, accurate research and testing data with clear traceability back to the original inquiry.
            """),
            show_tool_calls=True,
            show_members_responses=True,
            storage=research_testing_storage,
            add_history_to_messages=True,
            enable_user_memories=True,
            memory=research_testing_memory,
            **kwargs
        )
    
    @classmethod
    def observability_metrics(cls):
        return contextual_relevancy_metrics()
