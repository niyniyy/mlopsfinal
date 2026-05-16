import pytest
from src import model

def test_model_runs():
    # Just check that training runs without error
    try:
        model.main()  # assumes you wrapped your code in main()
    except Exception as e:
        pytest.fail(f"Model failed with error: {e}")
