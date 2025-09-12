from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno_test.utils.models import mistral_small_32_online


def create_healthcare_storage(db_file: str, table_name: str) -> SqliteStorage:
    """Create a standardized storage instance for healthcare components."""
    return SqliteStorage(table_name=table_name, db_file=db_file)


def create_healthcare_memory(db_file: str, table_name: str) -> Memory:
    """Create a standardized memory instance for healthcare components."""
    return Memory(
        model=mistral_small_32_online(),
        db=SqliteMemoryDb(table_name=table_name, db_file=db_file),
    )


def create_storage_and_memory(component_name: str):
    """Create both storage and memory for a healthcare component."""
    db_file = f"tmp/{component_name}.db"
    storage = create_healthcare_storage(db_file, f"{component_name}_sessions")
    memory = create_healthcare_memory(db_file, f"{component_name}_memories")
    return storage, memory
