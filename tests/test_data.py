"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

import common_access_model.datamodel.common_access_model_pydantic as pydantic_models

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))


def _load_model(filepath):
    """Load a YAML file into the Pydantic class named by the filename prefix."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(pydantic_models, target_class_name)
    with open(filepath) as f:
        data = yaml.safe_load(f)
    return tgt_class.model_validate(data)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Valid example files should load without error."""
    assert _load_model(filepath)


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Invalid example files should fail validation."""
    with pytest.raises(ValidationError):
        _load_model(filepath)
