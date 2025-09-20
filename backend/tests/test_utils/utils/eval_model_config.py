class EvalModelConfig:
    """Configuration class for managing the model."""
    _model = None  # Default model

    @classmethod
    def get_model(cls):
        """Get the current model."""
        return cls._model

    @classmethod
    def set_model(cls, model):
        """Set a new model."""
        cls._model = model
