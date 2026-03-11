from src.agentic.agents.differential_diagnosis_agent.schemas import DifferentialDiagnosisResponse
from src.common.models.models import LanguageModelFactory
from src.agentic.agents.differential_diagnosis_agent.prompts import differential_diagnosis_agent_description, differential_diagnosis_agent_instructions
from tests.test_utils.instrumentation.implementations.agno_inheritance import InstrumentedAgent
from tests.test_utils.utils.eval_metrics import answer_relevancy_metrics


class DifferentialDiagnosisAgent(InstrumentedAgent):
    """
    Agent specialized in performing differential diagnosis following clinical methodology.
    
    This agent follows the 4-step differential diagnosis process:
    1. Gather relevant information about medical history and present signs/symptoms
    2. List possible causes (candidate conditions) for the symptoms
    3. Prioritize the list by balancing risks with probability
    4. Recommend tests to determine actual diagnosis ("Rule Out" process)
    
    Uses the VINDICATEM mnemonic for systematic consideration of pathological processes:
    - Vascular, Inflammatory/Infectious, Neoplastic, Degenerative/Deficiency/Drugs,
    - Idiopathic/Intoxication/Iatrogenic, Congenital, Autoimmune/Allergic/Anatomic,
    - Traumatic, Endocrine/Environmental, Metabolic
    
    Inherits from the base Agent class in agno.
    """
    
    def __init__(self, name: str = "Differential Diagnosis Agent", **kwargs):
        """
        Initialize the Differential Diagnosis Agent.
        
        Args:
            name: The name of the agent
            **kwargs: Additional arguments passed to the base Agent class
        """
        super().__init__(
            name=name,
            description=differential_diagnosis_agent_description,
            instructions=differential_diagnosis_agent_instructions,
            model=LanguageModelFactory.create_default_model(),
            output_schema=DifferentialDiagnosisResponse,
            **kwargs
        )

    @classmethod
    def observability_metrics(cls):
        return answer_relevancy_metrics()
