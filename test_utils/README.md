uv run deepeval login --confident-api-key ""

# Run DeepEval test run with JUnit XML output
# Retries are now handled via custom logic in conftest.py
uv run deepeval test run test_evaluation.py --tb=short --disable-warnings --use-cache --num-processes=4 --identifier="Healthcare Demo"