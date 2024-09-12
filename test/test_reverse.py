import pytest
from my_package.my_module import reverse

@pytest.fixture(scope="session")
def sample_data():
    return "sample data"



def test_sample_data(sample_data):
    assert reverse(sample_data) == "-----------atad elpmas-----------"