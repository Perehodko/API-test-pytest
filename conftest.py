import pytest
from framework.helper import get_all_post, delete_post, gen_create_post
from framework.data.constants.smoke_consts import USER_IDS, TITLE, BODY_RESOURCE
from framework.jsonplaceholder_client import Client
from framework.check import response_general_check, check_create_resource


@pytest.fixture(scope='function')
def prepared_resource_id(request, post_exist=None):
    response = get_all_post()
    post_id = request.param

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


@pytest.fixture(scope='function')
def create_post(request, post_exist=None):
    response = get_all_post()
    post_id = request.param

    try:
        if response.json()[post_id]:
            post_exist = True
    except IndexError:
        post_exist = False

    if not post_exist:
        gen_create_post(post_id=request.param)

    def _clean_up():
        if post_exist:
            delete_post(post_id=request.param)

    request.addfinalizer(_clean_up)
    return request.param
