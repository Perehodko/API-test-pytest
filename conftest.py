import pytest
from framework.helper import get_all_post, delete_post


@pytest.fixture
def input_value():
    nonexist_resourse = "101"
    return nonexist_resourse


@pytest.fixture(scope='function')
def prepared_resource_id(request, post_exist=None):
    response = get_all_post()

    try:
        if response.json()[1]:
            post_exist = True
    except IndexError:
        post_exist = False

    if post_exist:
        delete_post(1)

    def _clean_up():
        if not post_exist:
            delete_post(1)
    request.addfinalizer(_clean_up)
