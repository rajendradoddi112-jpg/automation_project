import json
import os

import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir="reports"
    os.makedirs(report_dir,exist_ok=True)
    now=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    config.option.htmlpath=f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")

@pytest.fixture
def load_test_data():
    json_file_path=os.path.join(os.path.dirname(__file__),"data","Auth_post_payload.json")
    with open(json_file_path) as json_file:
        data=json.load(json_file)
        return data
    
@pytest.fixture
def load_put_data():
    json_file_path=os.path.join(os.path.dirname(__file__),"data","put_payload.json")
    with open(json_file_path) as json_file:
        data=json.load(json_file)
        return data

@pytest.fixture
def load_delete_data():
    json_file_path=os.path.join(os.path.dirname(__file__),"data","delete_payload.json")
    with open(json_file_path) as json_file:
        data=json.load(json_file)
        return data