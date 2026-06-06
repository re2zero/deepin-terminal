# autotest conftest
# App-specific fixtures go here.

import pytest


def pytest_addoption(parser):
    parser.addini("yaml_files", "Directory for YAML test files", type="pathlist")
