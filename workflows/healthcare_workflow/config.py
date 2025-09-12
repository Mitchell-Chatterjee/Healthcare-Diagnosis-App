from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno_test.utils.models import mistral_small_32_online

def setup_workflow_storage_and_memory():
    """Setup storage and memory configurations for the workflow."""
    # Database file for memory and storage
    workflow_db_file = "tmp/workflow_storage.db"
    
    # Session storage saves a Team's sessions in a database and enables Teams to have multi-turn conversations.
    storage = SqliteStorage(table_name="workflow_storage", db_file=workflow_db_file)
    
    memory = Memory(
        # Use any model for creating memories
        model=mistral_small_32_online(),
        db=SqliteMemoryDb(table_name="workflow_memories", db_file=workflow_db_file),
    )
    
    return storage, memory

class WorkflowConfig:
    """Configuration class for the Healthcare Workflow."""
    
    def __init__(self, use_storage: bool = True):
        self.use_storage = use_storage
        if use_storage:
            self.storage, self.memory = setup_workflow_storage_and_memory()
        else:
            self.storage = None
            self.memory = None
    
    @property
    def name(self):
        return "Healthcare Workflow"
    
    @property 
    def description(self):
        return "A workflow that orchestrates healthcare agents for symptom extraction, research, testing, and diagnosis."
