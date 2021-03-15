import pytest
from framework.jsonplaceholder_client import Client
from framework.check import _response_general_check

@pytest.fixture
def input_value():
    nonexist_resourse = "101"
    return nonexist_resourse


@pytest.fixture(scope='function')
def prepared_resource_id(request):
    response = Client().get_post_by_id(1)
    _response_general_check(response)
    post_id = response.json()['id']

    response = Client().delete(1)
    _response_general_check(response)



    def _clean_up():
        pass
    request.addfinalizer(_clean_up)