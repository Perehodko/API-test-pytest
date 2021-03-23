import pytest
from framework.helper import get_all_post, delete_post


@pytest.fixture
def input_value():
    nonexist_resourse = "101"
    return nonexist_resourse


@pytest.fixture(scope='function')
def prepared_resource_id(request, post_exist=None):
    response = get_all_post()
    post_id= request.param

    try:
        if response.json()[post_id]:
            post_exist = True
    except IndexError:
        post_exist = False

    if post_exist:
        delete_post(post_id=request.param)

    def _clean_up():
        if not post_exist:
            delete_post(post_id=request.param)
    request.addfinalizer(_clean_up)
    return request.param

