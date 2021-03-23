import allure
import pytest
from framework.jsonplaceholder_client import Client
from framework.check import response_general_check
from framework.data.constants.smoke_consts import USER_IDS


@pytest.mark.skip(reason='Not finished test')
@allure.suite('PUT /posts/{post_id}')
@allure.title('Positive. Update a resource')
def test_update_resource():
    data = {
        'id': 1,
        'title': 'New title for post',
        'body': 'New body for post',
        'userId': USER_IDS[0],
    }
    response = Client().update_post(USER_IDS[0], data)
    response_general_check(response)
