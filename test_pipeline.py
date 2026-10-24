import os
import pytest

def test_data_yaml_exists():
    assert os.path.exists("data/raw/data.yaml") or os.path.exists("../data/raw/data.yaml"), "data.yaml missing"

def test_weights_exist():
    weights_path = r"C:\Users\kusha\runs\detect\pork_tray_inspection-2\weights\best.pt"
    assert os.path.exists(weights_path), "Trained best.pt model weights missing"